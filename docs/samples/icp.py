import numpy as np
import pcl
from pcl import IterativeClosestPoint
import time

start_time = time.time()


src = "/home/ajay/icp_test/deg_1.5/src.pcd"
trans = "/home/ajay/icp_test/deg_1.5/trans.pcd"
p1 = pcl.load(src)
p2 = pcl.load(trans)


def computeICPDelta(source, target, iters=50):
    global currMap
    source_array = source.to_array()
    target_array = target.to_array()

    source_min_array = source_array[np.where((abs(source_array[:,0]) < 20) &
                       (abs(source_array[:,1]) < 20))]
    target_min_array = target_array[np.where((abs(target_array[:,0]) < 20) &
                       (abs(target_array[:,1]) < 20))]

    source_min_cloud = pcl.PointCloud(source_min_array)
    target_min_cloud = pcl.PointCloud(target_min_array)
    print(len(source_min_array))
    print(len(target_min_array))

    icp = source_min_cloud.make_IterativeClosestPoint()
    if ((source_min_cloud.size > 0) & (target_min_cloud.size > 0)):
        converged, transf, estimate, fitness = icp.icp(source_min_cloud, target_min_cloud, max_iter=iters)
        print(converged, estimate, fitness)
        print(icp)
        if (converged):
            if (fitness < 0.2):
                print("Fitness quality ok")
            print(transf)
        else:
            print("ICP fails to converge")
    else:
        print("No points for ICP")
        # transf = nbconvert_exporter

    return transf


def main():
    result = computeICPDelta(p1, p2)
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == main():
    main()
