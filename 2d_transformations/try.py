import numpy as np
import math


net_transform = np.identity(3)


def rotate(transformation_angle):
    transformation_angle = transformation_angle * math.pi / 180
    sine = math.sin(transformation_angle)
    cosine = math.cos(transformation_angle)
    rotation = np.identity(3)
    rotation[0][0] = cosine
    rotation[0][1] = -sine
    rotation[1][0] = sine
    rotation[1][1] = cosine
    return rotation


def scale(sx, sy):
    scaling = np.identity(3)
    scaling[0][0] = sx
    scaling[1][1] = sy
    return scaling


def translate(tx, ty):
    translation = np.identity(3)
    translation[0][2] = tx
    translation[1][2] = ty
    return translation


x_values = [1, 2, 3]
y_values = [1, 3, 4]
w_values = list()

if len(x_values) == len(y_values):
    for i in range(len(x_values)):
        w_values.append(1)

x_string = ' '.join(str(val) for val in x_values)
y_string = ' '.join(str(val) for val in y_values)
w_string = ' '.join(str(val) for val in w_values)

data_string = x_string + '; ' + y_string + '; ' + w_string
data = np.matrix(data_string)

net_transform = net_transform.dot(rotate(-90))
print "After rotation, transformation matrix is:"
print net_transform

net_transform = net_transform.dot(translate(10, 10))
print "After translation, transformation matrix is:"
print net_transform

net_transform = net_transform.dot(scale(2, 2))
print "After scaling, transformation matrix is:"
print net_transform

print "Resultant matrix is:"
print net_transform.dot(data)

