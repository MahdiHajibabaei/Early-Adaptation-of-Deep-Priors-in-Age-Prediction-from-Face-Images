
# This script is supposed to be run on a single GPU and evaluate the MAE scores of the fine_tunings along the non-fine-tuned network and write the result in a CSV

import os
#import sys
#import argparse
#import glob
#import time

import numpy as np
#import matplotlib.pyplot as plt
#from PIL import Image
#os.environ["GLOG_minloglevel"] = "2"
import caffe

print 'Caffe imported successfully!'
GPU_ID=1
caffe.set_device(GPU_ID)
caffe.set_mode_gpu()

Model_name='LAP_100_full'
base_address='/srv/glusterfs/hmahdi/IMDB/learning_curve_snapshots/'
#base_address='/srv/glusterfs/hmahdi/IMDB/models/snapshots/'
outputfile = open(Model_name+'.csv','w+')
for root, dirs, files in os.walk(base_address):
    for file in files:
        if (file.endswith(".caffemodel")):   #and file.startswith(Model_name)) :
		Caffe_model=base_address+file
		net = caffe.Net('/home/hmahdi/caffe/examples/imdb/Pre-training_distribution/age_MAE.prototxt',Caffe_model, caffe.TEST)
		# This part does the MAE evaluation on the ChaLearn validation set (1136 samples)
		j=np.arange(101)
		MAE_accumulator=0
		test_set_size=1136
		for batch_number in xrange(0,16):
			out = net.forward()
			for i in xrange(0,71):
				predicted_age=np.dot(out['prob'][i],j)
				expected_age=out['label'][i]
				MAE_accumulator+=np.absolute(predicted_age-expected_age)
		
		print file
		print MAE_accumulator/test_set_size
		outputfile.write(file+','+str(MAE_accumulator/test_set_size)+'\n')
		del net 
	





