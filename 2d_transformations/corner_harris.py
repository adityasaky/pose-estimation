import pcl
import numpy as np
import cv2
from matplotlib import pyplot as plt


source1 = "../pointclouds/10.jpg"
source2 = "../pointclouds_filtered/20.0_20.0_0.1/10-20.0_20.0_0.1.jpg"

img1 = cv2.imread(source1, 0)
img1 = np.float32(img1)
corners1 = cv2.cornerHarris(img1, 2, 3, 0.4)
plt.imshow(corners1)
plt.show()

count = 0
for row in corners1:
    for col in row:
        if col != 0.0:
            count += 1
print(count)

img2 = cv2.imread(source2, 0)
img2 = np.float32(img2)
corners2 = cv2.cornerHarris(img2, 2, 3, 0.4)
plot2 = plt.imshow(corners2)
plt.show()

count = 0
for row in corners2:
    for col in row:
        if col != 0.0:
            count += 1
print count
