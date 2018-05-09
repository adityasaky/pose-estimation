import numpy as np
import csv
import math

count = 0
line_no = 0
delta_x = []
delta_y = []
yaw_angle = []

csv_path = "/home/anagha/fyproject/Data_2_21_pos_n_yaw.txt"
f_obj = open(csv_path, "r")
reader = csv.reader(f_obj)
for row in reader:
   line_no = line_no + 1
   if (line_no % 10 == 1):
       delta_x.append(float(row[0].split(' ')[0]))
       delta_y.append(float(row[0].split(' ')[1]))
       yaw_angle.append(float(row[0].split(' ')[2]))

print(len(delta_x))
np.array(delta_x)
np.array(delta_y)
np.array(yaw_angle)

for i in range(0,434):
    delta_yaw_angle = yaw_angle[i+1] - yaw_angle[i]
    if math.degrees(delta_yaw_angle) > 0 and math.degrees(delta_yaw_angle) <= 10.0:
        print("---")
        count = count + 1
        print(count)
        print(math.degrees(delta_yaw_angle))
        print(i)
        print(i+1)

