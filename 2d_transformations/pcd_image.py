import pcl
import numpy as np
import cv2
import sys
import os

source_directory = "../training_data/"

height = 160
width = 160

heightMeters = 80
widthMeters = 60


def scalex(x):
    global height, width

    xs = int(width * (widthMeters * 0.5 + x) / widthMeters)

    return xs


def scaley(y):
    # ys = int(height * y  / heightMeters )
    ys = int(height * (heightMeters * 0.5 + y) / heightMeters)

    return height - 1 - ys


def map_to_image(x, y, z, avgHeight):
    global height, width

    img = np.zeros((height, width, 3), np.uint8)
    for i in range(len(x)):
        # if abs(z[i]) >= avgHeight + 0.5:
        if (abs(x[i]) <= widthMeters * 0.5) & (abs(y[i]) <= heightMeters * 0.5):
            xs = scalex(x[i])
            ys = scaley(y[i])
            img[ys, xs, 0] = 255
            img[ys, xs, 1] = 255
            img[ys, xs, 2] = 255

    return img


if len(sys.argv) >= 2:
    sub_directory = sys.argv[1]
else:
    print "Error"
    sys.exit()



if sub_directory:
    for folder in os.listdir(source_directory):
        for pcd_file in os.listdir(source_directory + folder):
            if not pcd_file.endswith('.pcd'):
                continue
            cloud = pcl.load(source_directory + folder + "/" + pcd_file)
            pt_ar = cloud.to_array()
            x = pt_ar[:, 0]
            y = pt_ar[:, 1]
            z = pt_ar[:, 2]
            avg_height = np.mean(z)
            img = map_to_image(x, y, z, avg_height)
            jpg_file = pcd_file.split('.pcd')[0] + ".jpg"
            cv2.imwrite(source_directory + folder + "/" + jpg_file, img)
else:
    for pcd_file in os.listdir(source_directory):
        if not pcd_file.endswith('.pcd'):
            continue
        cloud = pcl.load(source_directory + pcd_file)
        pt_ar = cloud.to_array()
        x = pt_ar[:, 0]
        y = pt_ar[:, 1]
        z = pt_ar[:, 2]
        avg_height = np.mean(z)
        img = map_to_image(x, y, z, avg_height)
        jpg_file = pcd_file.split('.pcd')[0] + ".jpg"
        cv2.imwrite(jpg_file, img)
