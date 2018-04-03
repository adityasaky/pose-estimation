import pickle
import os


for f in os.listdir('pickle_files'):
    if f.endswith('.pkl'):
        with open("pickle_files/" + f, "r") as file_open:
            print(pickle.load(file_open))