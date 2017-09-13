
# This script is written to only change the directory of dataset if the folder containing images are moved
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re
from random import shuffle
import pickle
import random

direcotry='Learning_curve_source_files/'
datasets=['2_1_aug_train.txt','2_1_train.txt','2_1_test.txt']
for dataset in datasets:
	dataset_path=direcotry+dataset	
	#Preparing the Network description prototxt
	with open(dataset_path, 'r') as file :
  		filedata = file.read()
	filedata = filedata.replace('/rrothe/','/aeirikur/rrothe/')
	with open(dataset, 'w') as file:
  		file.write(filedata)	

