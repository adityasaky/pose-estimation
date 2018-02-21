import os
import pickle
import numpy as np


source_directory = "../pointclouds/"
training_directory = "../training_data/"
transformations_directory = "./pickle_files/"

for pcd_file in os.listdir(source_directory):
    with open(source_directory + pcd_file, 'r') as f:
        all_points = f.readlines()[11:]
        source_name = pcd_file.split('.')[0]
        target_directory = training_directory + source_name + '/'
        print 'Reading ' + source_name + '...'
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        for pkl_file in os.listdir(transformations_directory):
            with open(transformations_directory + pkl_file, 'r') as t:
                transformation = pickle.load(t)
                transformation_name = pkl_file.split('.')[0]
                target_name = source_name + '_' + transformation_name + '.pcd'
                print 'Performing ' + transformation_name + '...'
                count = 0
                all_lines = list()
                for point in all_points:
                    point_list = point.split(' ')
                    if -10.0 <= float(point_list[0]) <= 10.0 and -10.0 <= float(point_list[1]) <= 10.0:
                        count += 1
                        data = np.matrix(point_list[0] + ' ; ' + point_list[1] + ' ; ' + '1')
                        transformation_result = np.dot(transformation, data)
                        x = str(transformation_result[0, 0])
                        y = str(transformation_result[1, 0])
                        z = '0'
                        row = x + ' ' + y + ' ' + z + '\n'
                        all_lines.append(row)
            with open(target_directory + target_name, 'w') as o:
                o.write("# .PCD v0.7 - Point Cloud Data file format\n")
                o.write("VERSION 0.7\n")
                o.write("FIELDS x y z\n")
                o.write("SIZE 4 4 4\n")
                o.write("TYPE F F F\n")
                o.write("COUNT 1 1 1\n")
                o.write("WIDTH " + str(count) + "\n")
                o.write("HEIGHT 1\n")
                o.write("VIEWPOINT 0 0 0 1 0 0 0\n")
                o.write("POINTS " + str(count) + "\n")
                o.write("DATA ascii\n")
                o.writelines(all_lines)