
# This script is supposed to be run on a single GPU and evaluate the MAE scores of the fine_tunings along the non-fine-tuned network and write the result in a CSV

import os
#import sys
#import argparse
#import glob
#import time

import numpy as np
#import matplotlib.pyplot as plt
#from PIL import Image
import re

Model_name='Learning_curve_results/MORPH_10000_full_extension'
base_address='/srv/glusterfs/hmahdi/IMDB/learning_curve_snapshots/'
portions=[]
sorted_data=[[]]
#base_address='/srv/glusterfs/hmahdi/IMDB/models/snapshots/'
outputfile = open(Model_name+'.csv','r')
for line in outputfile:
	parsed_line=re.split(r'[_,\n-]+', line)
	#print parsed_line
	#print parsed_line[2]+' '+ parsed_line[6]
	if parsed_line[2] in portions:
		p_index=portions.index(parsed_line[2])
		sorted_data[p_index].append(float(parsed_line[6]))
	else: 
		portions.append(parsed_line[2])
		sorted_data.append([])
		p_index=portions.index(parsed_line[2])
		sorted_data[p_index].append(float(parsed_line[6]))
i=0
for data_point in sorted_data:
	print str(portions[i])+'  '+str(np.mean(data_point))+'  '+str(np.std(data_point))
	#print np.mean(data_point)
	#print np.std(data_point)
	i+=1



