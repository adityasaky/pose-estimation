import numpy as np
import cv2
import pcl
import glob

# start with an image 160 X 120
img1 = np.ndarray(shape=(160,100), dtype=int)
img2 = np.ndarray(shape=(160,100), dtype=int)
print(img1.shape)
print(img2.shape)
# Reshape them to 15X65X20
img1_nshp = np.reshape(img1, (16, 20, 50))
img2_nshp = np.reshape(img2, (16, 20, 50))
print(img1_nshp.shape)
print(img2_nshp.shape)
# Concatenate images ..
img_concat = np.concatenate((img1_nshp, img2_nshp), axis=2)
img_concat.shape

# Open a PCD file and convert (rescale) to 160X120 ..
height = 160 
width = 120 

heightMeters = 80
widthMeters = 60


# X axis max is heightMeters metres on either side
# so 120 pixels converts to 120 on +x and 120 -x
def scalex(x) :
    global height, width
    
    xs = int(width * (widthMeters * 0.5 + x) / widthMeters)
    
    return xs


# Y axis max is 80 metres 
# so 160 => 80 mtr
# use decimeter to preserve first decimal for accuracy
def scaley(y) :
    #ys = int(height * y  / heightMeters )
    ys = int(height * (heightMeters * 0.5 + y) / heightMeters)
    
    return height -1 - ys
    #return ys


# Convert a PCD file to an img file (height X width) and 80 X 60 mts
# all points outside this range marked out of image
def XYToImage(x, y, z, avgHeight) :
    global height, width
    
    img = np.zeros((height, width, 3), np.uint8)
    for i in range(len(x)) :
        if (abs(z[i]) >= avgHeight + 0.5) :
            if ((abs(x[i]) <= widthMeters * 0.5) & (abs(y[i]) <= heightMeters * 0.5)) :
                xs = scalex(x[i])
                ys = scaley(y[i])
                img[ys, xs,  0] = 255
                img[ys, xs,  1] = 255
                img[ys, xs, 2] = 255
        
    return img


'''
file = '/home/prasad/lidar_m8_data/run_indoor_set2/non-ground/181.pcd'
cloud = pcl.load(file)
ptAr = cloud.to_array()
x = ptAr[:, 0]
y = ptAr[:, 1]        
z = ptAr[:, 2]
avgHeight = np.mean(z)
img = XYToImage(x, y, z, avgHeight)
jpgFile = file.split('.pcd')[0] + ".jpg"
print(jpgFile, jpgFile)
cv2.imwrite(jpgFile, img)
'''

# reads all pcds in a dir and converts to jpg
# writes out the jpg file as 1.pcd.jpg
dir = '../../pointclouds/'
fileList = glob.glob(dir + '*.pcd')
for file in fileList:
    cloud = pcl.load(file)
    ptAr = cloud.to_array()
    x = ptAr[:, 0]
    y = ptAr[:, 1]        
    z = ptAr[:, 2]
    avgHeight = np.mean(z)
    img = XYToImage(x, y, z, avgHeight)
    jpgFile = file.split('.pcd')[0] + ".jpg"
    cv2.imwrite(jpgFile, img)
