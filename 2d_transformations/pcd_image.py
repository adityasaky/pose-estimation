import pcl
import numpy as np
import os
import cv2

source_directory = "../training_data"
destination = "/home/ajay/img_data"

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


def xyToimage(x, y, z, avgHeight):
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


for source, dirs, files in os.walk(source_directory):
    for file in files:
        # file = '1000.pcd'
        cloud = pcl.load(files)
        ptAr = cloud.to_array()
        x = ptAr[:, 0]
        y = ptAr[:, 1]
        z = ptAr[:, 2]
        avgHeight = np.mean(z)
        img = xyToimage(x, y, z, avgHeight)
        jpgFile = files.split('.pcd')[0] + ".jpg"
        cv2.imwrite(jpgFile, img)
        # print(files)
