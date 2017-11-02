
# This script prepares all the files needed for the part one of the experiment; different experiments can be designed by only changing the parameters in this script.
# Warning: if the datasets are recreated the results will be diffrent because the random re-sampling used would yield tha same datasets.

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re
from random import shuffle
import pickle
import random

#Current working directory of this python script
CWD='/home/hmahdi/caffe/examples/imdb/Pre-training_distribution/'
# 80% of the ChaLearn training set augmented with 11 rotations used as training set 1981*11 samples
Trainlist='/home/hmahdi/caffe/examples/imdb/Pre-training_distribution/chalearn_aug_train_80.txt'
# 20% of the ChaLearn training set not augmented 495 samples used as validation set
Validationlist='/home/hmahdi/caffe/examples/imdb/Pre-training_distribution/chalearn_train_20.txt'
# Whether to recreate the datasets or not
Recreate_datasets=False

Trainfile = open(Trainlist,'r')
Validationfile = open(Validationlist,'r')

entry_array=[]
sample_number=0
for line in Trainfile:
	sample_number+=1
	entry_array.append(line)

validation_array=[]
validation_number=0
for line in Validationfile:
	validation_number+=1
	validation_array.append(line)

print 'The size of Training set is '+str(sample_number)
print 'The size of Validation set is '+str(validation_number)
# This part of code bundles all the augmentations of the same image together
entry_array=sorted(entry_array, key=str.lower)
sample_number/=11
entry_array=np.reshape(entry_array,(sample_number,11))
sample_index=range(sample_number)

validation_index=range(validation_number)
# Experiment settings the portions of ChaLearn dataset used, number of iterations for each portion, step size for reducing the learning rate, and maximum itaration of training 
portions=[[0.005,32],[0.01,16],[0.02,8],[0.04,4],[0.08,2],[0.16,1],[0.2,1],[0.4,1],[0.8,1]]
stepsize=["13","25","50","100","200","400","500","1000","2000"]
max_iter=["65","125","250","500","1000","2000","2500","5000","10000"]

i=0
for p in portions:
	for index in xrange(0,p[1]):
		
		# Re-sample from big train set to create training set
		base_address='Learning_curve_datasets/'
		Training_set_address=base_address+'finetune_train_'+str(p[0])+'_'+str(index)+'.txt'
		if Recreate_datasets:
			subset_entry_array=[]
			chosen_index=(np.random.choice(sample_index,size=int(sample_number*p[0]/0.8),replace=False))
			for j in chosen_index:
				subset_entry_array.extend(entry_array[j])	
			shuffle(subset_entry_array)
		
			finetune_dataset = open(Training_set_address,'w+')
			for item in subset_entry_array:
 				finetune_dataset.write("%s" % item)
			del subset_entry_array

		#Re-sample from big validation set to create validation set
		base_address='Learning_curve_datasets/'
		Validation_set_address=base_address+'finetune_validation_'+str(p[0])+'_'+str(index)+'.txt'
		if Recreate_datasets: 
			subset_entry_array=[]
			chosen_index=(np.random.choice(validation_index,size=int(validation_number*p[0]/0.8),replace=False))
			for j in chosen_index:
				subset_entry_array.append(validation_array[j])	
			shuffle(subset_entry_array)
			finetune_dataset = open(Validation_set_address,'w+')
			for item in subset_entry_array:
 				finetune_dataset.write("%s" % item)
			del subset_entry_array
		
		#Preparing the Network description prototxt
		with open('age_train.prototxt', 'r') as file :
  			filedata = file.read()
		Training_set_address=CWD+Training_set_address
		Validation_set_address=CWD+Validation_set_address
		filedata = filedata.replace('Train_set',Training_set_address)
		filedata = filedata.replace('Validation_set',Validation_set_address)
		Network_address='Learning_curve_prototxts_2/DEX_'+str(p[0])+'_'+str(index)+'.prototxt'
		with open(Network_address, 'w') as file:
  			file.write(filedata)	

		#Create the solvers
		Network_address=CWD+Network_address
		Solver_address='Learning_curve_prototxts_2/DEX_solver_'+str(p[0])+'_'+str(index)+'.prototxt'
		solver_text = open(Solver_address,'w+')
		solver_text.write("net: \""+Network_address+"\"\n")
		solver_text.write("test_state: {stage: 'test-on-train'}\n")
		solver_text.write("test_iter: 45\n")
		solver_text.write("test_state: {stage: 'test-on-test'}\n")
		solver_text.write("test_iter: 71\n")
		solver_text.write("test_interval: "+stepsize[i]+"\n")
		solver_text.write("base_lr: 0.000100\n")
		solver_text.write("lr_policy: \"step\"\n")
		solver_text.write("gamma: 0.100000\n")
		solver_text.write("stepsize: "+stepsize[i]+"\n")
		solver_text.write("display: 100\n")
		solver_text.write("max_iter: "+max_iter[i]+"\n")
		solver_text.write("momentum: 0.9\n")
		solver_text.write("weight_decay: 0.0005\n")
		solver_text.write("snapshot: "+max_iter[i]+"\n")
		solver_text.write("snapshot_prefix: \"/srv/glusterfs/hmahdi/IMDB/learning_curve_snapshots_2/Fine_tune_"+str(p[0])+'_'+str(index)+"\"\n")
		solver_text.write("solver_mode: GPU\n")

	i+=1
		

