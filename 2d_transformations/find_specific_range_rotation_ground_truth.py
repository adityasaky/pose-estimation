import numpy as np
import os
import shutil


ground_truth_file= "../docs/ground_truth.txt"
sample_directory = "/home/saky/tmp/test_data_pairs/"
target_directory = "/home/saky/tmp/test_data_pairs_10_5_5/"
ground_truth = open(ground_truth_file, "r").readlines()
i = 10
samples = list()
while i < len(ground_truth):
    print(i)
    j = i + 10
    if j > len(ground_truth):
        break
    ground_truth_i = ground_truth[i-1].split(" ")
    ground_truth_j = ground_truth[j-1].split(" ")
    theta_i = float(ground_truth_i[2])
    theta_j = float(ground_truth_j[2])
    tx_i = float(ground_truth_i[0])
    tx_j = float(ground_truth_j[0])
    ty_i = float(ground_truth_i[1])
    ty_j = float(ground_truth_j[1])
    theta_del = np.rad2deg(theta_j - theta_i)
    tx_del = tx_j - tx_i
    ty_del = ty_j - ty_i
    if 0.0 <= abs(theta_del) <= 10.0 and 0.0 <= abs(tx_del) <= 5.0 and 0.0 <= abs(ty_del) <= 5.0:
        sample_name = str(i) + "_" + str(j) + ".npz"
        samples.append(sample_name)
    i += 10


print(samples)

for npz in samples:
    if os.path.exists(sample_directory + npz):
        shutil.copy(sample_directory + npz, target_directory + npz)

