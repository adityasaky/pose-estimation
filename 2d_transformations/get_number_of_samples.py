import numpy as np
import os


source = "../dataset_h4_half_deg/"
count = 0
for npz_file in os.listdir(source):
    archive = np.load(source + npz_file)
    count += len(archive['truth'])
    del archive
print(count)
