import os
import pickle
import numpy as np
import pcl


source_directory = "../pointclouds/"
training_directory = "../training_data/"
transformations_directory = "./pickle_files/"

x_limit = 20.0
y_limit = 20.0
z_limit = 0.1

for pcd_file in os.listdir(source_directory):
    source_name = pcd_file.split('.')[0]
    print "Reading " + source_name
    all_points = pcl.load(source_directory + pcd_file)
    all_points_array = all_points.to_array()
    target_directory = training_directory + source_name + '/'
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    print "Filtering points"
    filtered_points_array = all_points_array[np.where((abs(all_points_array[:, 0]) < x_limit) & (abs(all_points_array[:, 1]) < y_limit) & (all_points_array[:, 2] >= z_limit))]
    filtered_points_matrix = np.matrix(filtered_points_array)
    for pkl_file in os.listdir(transformations_directory):
        with open(transformations_directory + pkl_file, 'r') as t:
            transformation = pickle.load(t)
            transformation_name = pkl_file.split('.')[0]
            target_name = source_name + "-" + transformation_name + ".pcd"
            print "Performing " + transformation_name
            transformation_result_matrix = np.dot(filtered_points_matrix, transformation)
            transformation_result_array = np.array(transformation_result_matrix)
            transformation_result = pcl.PointCloud()
            transformation_result.from_array(transformation_result_array)
            print "Writing " + target_name
            transformation_result.to_file(target_directory + target_name)

'''
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
                    if -x_limit <= float(point_list[0]) <= x_limit and -y_limit <= float(point_list[1]) <= y_limit:
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
'''