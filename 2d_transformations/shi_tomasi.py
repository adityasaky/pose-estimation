import pcl
import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob

'''
source1 = "../pointclouds/10.jpg"

img1 = cv2.imread(source1, 0)
img1 = np.float32(img1)
corners1 = cv2.goodFeaturesToTrack(img1,300,0.01,10,None,3,0,0.04 )
corners1 = np.int0(corners1)

for i in corners1:
    x,y = i.ravel()
    cv2.circle(img1, (x, y), 3, 255, -1)
plt.imshow(img1)
plt.show()
'''
dir = "../pointclouds_filtered/20.0_20.0_0.1/voxel_filtered/0.5_0.5_0.5/"
fileList = glob.glob(dir + '*.jpg')
for jpg_file in fileList:
	img = cv2.imread(jpg_file, 0)
	img = np.float32(img)
	corners = cv2.goodFeaturesToTrack(img,300,0.01,10,None,3,1,0.04)
	# corners = np.int0(corners)
	txt_file = jpg_file.split('.jpg')[0] + ".txt"
	f=open(txt_file,"w")
	f.write(str(corners))
	f.close()
	'''
	for i in corners2:
    	x,y = i.ravel()
    	cv2.circle(img2, (x, y), 3, 255, -1)
	plt.imshow(img2)
	plt.show()
	'''
