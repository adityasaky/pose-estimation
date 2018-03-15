import pcl
import os


x_leaf = 0.5
y_leaf = 0.5
z_leaf = 0.5

source_directory = "../pointclouds/"
target_directory = "../pointclouds/voxel_filtered/" + str(x_leaf) + "_" + str(y_leaf) + "_" + str(z_leaf) + "/"

for pcd_file in os.listdir(source_directory):
    if not pcd_file.endswith(".pcd"):
        continue
    cloud = pcl.load(source_directory + pcd_file)
    cloud_filter = cloud.make_voxel_grid_filter()
    cloud_filter.set_leaf_size(x_leaf, y_leaf, z_leaf)
    result = cloud_filter.filter()
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    pcl.save(result, target_directory + pcd_file.split('.')[0] + "-" + str(x_leaf) + "_" + str(y_leaf) + "_" + str(z_leaf) + ".pcd")
