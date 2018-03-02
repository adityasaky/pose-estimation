import os


x_limit = 10.0
y_limit = 10.0
source_directory = "../pointclouds/"
target_directory = "../pointclouds_filtered/" + str(x_limit) + "_" + str(y_limit) + "/"

for pcd_file in os.listdir(source_directory):
    with open(source_directory + pcd_file, 'r') as f:
        all_points = f.readlines()[11:]
        source_name = pcd_file.split('.')[0]
        print 'Reading ' + source_name + '...'
        target_name  = source_name + "_" + str(x_limit) + "_" + str(y_limit) + ".pcd"
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        count = 0
        all_lines = list()
        for point in all_points:
            point_list = point.split(' ')
            if -x_limit <= float(point_list[0]) <= x_limit and -y_limit <= float(point_list[1]) <= y_limit and float(point_list[2]) > -0.5:
                count += 1
                all_lines.append(point)
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