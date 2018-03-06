import pcl
import numpy as np
import cv2
from matplotlib import pyplot as plt


source1 = "../pointclouds/10.jpg"
source2 = "../pointclouds_filtered/20.0_20.0_0.1/10-20.0_20.0_0.1.jpg"

img1 = cv2.imread(source1, 0)
img1 = np.float32(img1)
corners1 = cv2.goodFeaturesToTrack(img1,1,0.01,10,None,3,0,0.04 )
corners1 = np.int0(corners1)

for i in corners1:
    x,y = i.ravel()
    cv2.circle(img1, (x, y), 3, 255, -1)
plt.imshow(img1)
plt.show()

img2 = cv2.imread(source2, 0)
img2 = np.float32(img2)
corners2 = cv2.goodFeaturesToTrack(img2,1,0.01,10,None,3,0,0.04)
corners2 = np.int0(corners2)

for i in corners2:
    x,y = i.ravel()
    cv2.circle(img2, (x, y), 3, 255, -1)
plt.imshow(img2)
plt.show()
