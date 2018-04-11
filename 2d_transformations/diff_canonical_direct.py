import numpy as np
import math
import pickle
import os, sys
import pcl


angle = 30
tx = 4
ty = 4

def rotate(angle):
    radian = angle * math.pi / 180.0
    rot_mat = np.identity(3)
    sine = math.sin(radian)
    cosine = math.cos(radian)
    rot_mat[0][0] = cosine
    rot_mat[0][1] = -sine
    rot_mat[1][0] = sine
    rot_mat[1][1] = cosine
    return rot_mat


def translate(distance_x, distance_y):
    trn_mat = np.identity(3)
    trn_mat[0][2] = distance_x
    trn_mat[1][2] = distance_y
    return trn_mat


rotation_matrix = rotate(angle)
translation_matrix = translate(tx, ty)
direct = np.dot(rotation_matrix, translation_matrix)
canonical = rotation_matrix
canonical[0, 2] = tx
canonical[1, 2] = ty
print("Direct Matrix:")
print(direct)
print("Canonical Matrix:")
print(canonical)

pcd = pcl.load('../pointclouds/1040.pcd')
pcd_matrix = np.transpose(np.matrix(pcd.to_array()))
canonical_result = np.array(np.transpose(np.dot(canonical, pcd_matrix)))
direct_result = np.array(np.transpose(np.dot(direct, pcd_matrix)))
canonical_pcd = pcl.PointCloud()
direct_pcd = pcl.PointCloud()
canonical_pcd.from_array(np.float32(canonical_result))
direct_pcd.from_array(np.float32(direct_result))
canonical_pcd.to_file('/home/saky/tmp/diff_canonical_direct/canonical.pcd')
direct_pcd.to_file('/home/saky/tmp/diff_canonical_direct/direct.pcd')
