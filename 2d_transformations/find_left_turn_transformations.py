import pickle
import os
import math

for f in os.listdir('/home/anagha/fyproject/1'):
    if f.endswith('.pkl'):
        with open("/home/anagha/fyproject/1/" + f, "rb") as file_open:
            file = pickle.load(file_open)

for element in file:
    #print("---")
    #print(element)
    #print("---")
    #print(file[element])
    #print("---")
    #print(file[element][0])
    #print("---")
    #print(file[element][0][0])
    #print("---")
    angle = math.acos(file[element][0][0])
    if angle > 0 and angle <= 10.0:
        print(element)
