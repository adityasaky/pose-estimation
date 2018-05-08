import pickle
import os
import math

for f in os.listdir('/home/anagha/fyproject/1'):
    if f.endswith('.pkl'):
        with open("/home/anagha/fyproject/1/" + f, "rb") as file_open:
            file = pickle.load(file_open)
            for pair in file:
                #print("---")
                #print(pair)
                #print("---")
                #print(file[pair])
                #print("---")
                #print(file[pair][0])
                #print("---")
                #print(file[pair][0][0])
                #print("---")
                angle = math.acos(file[pair][0][0])
                #print(angle)
                if angle >= 0.0 and angle <= 10.0:
                    print(pair)