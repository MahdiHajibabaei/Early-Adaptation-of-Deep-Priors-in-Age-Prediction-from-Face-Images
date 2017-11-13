
# This script is written to only change the directory of dataset if the folder containing images are moved
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re
from random import shuffle
import pickle
import random

directory='ChaLearn_datasets/'
datasets=['chalearn_aug_train_80.txt','chalearn_train_20.txt','chalearn_validation.txt']
previous_directory='/home/rrothe/git/chalearn/code/data/'
new_directory='/srv/glusterfs/aeirikur/rrothe/results/chalearn/chalearn_data/'
for dataset in datasets:
	dataset_path=directory+dataset	
	#Preparing the Network description prototxt
	with open(dataset_path, 'r') as file :
  		filedata = file.read()
	filedata = filedata.replace(previous_directory,new_directory)
	with open(dataset, 'w') as file:
  		file.write(filedata)	

