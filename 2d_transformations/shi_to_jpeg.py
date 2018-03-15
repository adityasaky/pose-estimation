import pcl
import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob

source1 = "../pointclouds/2030.jpg"
source = "2030.jpg"
count = 0
img4 = cv2.imread(source1, 0)
i=0

img4 = np.float32(img4)


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

# Open a PCD file and convert (rescale) to 160X120 ..
height = 160 
width = 160

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






corners1 = cv2.goodFeaturesToTrack(img4,300,0.01,10,None,3,0,0.04 )
#corners1 = np.int0(corners1)
rows = corners1.shape[0]
a = np.empty( shape=(rows,3))
l = []
for element in corners1.flat:
	l.append(element)

for x in xrange(0,rows):
	a[x][0] = l[i]
	i = i+1
	a[x][1] = l[i]
	i = i+1
	a[x][2] = 0
	
x = a[:, 0]
print "value is" + str(x)
y = a[:, 1]        
z = a[:, 2]
print "value is " + str(z)
avgHeight = np.mean(z)
img = XYToImage(x, y, z, avgHeight)
jpgFile = source.split('.jpg')[0] + ".jpg"
cv2.imwrite(jpgFile, img)
