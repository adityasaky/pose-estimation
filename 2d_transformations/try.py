import numpy as np
import math


def rotate(transformation_angle, data):
    transformation_angle = transformation_angle * math.pi / 180
    sine = math.sin(transformation_angle)
    cosine = math.cos(transformation_angle)
    transformation = np.identity(2)
    transformation[0][0] = cosine
    transformation[0][1] = -sine
    transformation[1][0] = sine
    transformation[1][1] = cosine
    print transformation.dot(data)


x_values = [1, 2, 3]
y_values = [1, 3, 4]

x_string = ' '.join(str(val) for val in x_values)
y_string = ' '.join(str(val) for val in y_values)

data_string = x_string + '; ' + y_string
data = np.matrix(data_string)

rotate(90, data)
