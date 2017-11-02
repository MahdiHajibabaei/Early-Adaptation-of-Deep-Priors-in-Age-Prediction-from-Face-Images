
# This script is supposed to evaluate the cross entropy of each dataset vs the LAP validation set and write this to a csv

import os
import scipy
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re


Net_output='/srv/glusterfs/hmahdi/IMDB/models/LAP_evaluations/test_output_LAP10epoch.txt'
inputfile = open(Net_output,'r')


#age_plot=np.zeros((101),dtype=float)
partial_distribution=np.zeros((101),dtype=float)
LAP_Validation_distribution=np.zeros((101),dtype=float)
Likelihood=0
batch_number=0
last_estimated_age=0
EstimatedAge=[]#estimated age
RealAge=[]
age=0


# LAP Validation set address
Imagelist='/home/hmahdi/caffe/examples/imdb/imdbwiki-0-101_1_test.txt'

inputfile = open(Imagelist,'r')
#age_array=np.empty((101,),dtype=np.object_)
#age_array.fill([])
#age_array = np.frompyfunc(list,1,1)(age_array)

age_distribution=np.zeros((101),dtype=float)
#print len(age_array)

sample_number=0
for line in inputfile:
	sample_number+=1
	parsed_line=re.split(' ', line, 1)
	#age=int(re.search(r' \d+', line).group())
	age=int(parsed_line[1]) 
	age_distribution[age]+=1
	#age_array[age].append(parsed_line[0])

print "Lap_Validation_set:"
print Imagelist
print sample_number
LAP_Validation_distribution=age_distribution/sample_number
del inputfile
del age_distribution



base_address='/home/hmahdi/caffe/examples/imdb/Pre-training_distribution/Learning_curve_datasets'
outputfile = open('Cross_entropies.csv','w+')
for root, dirs, files in os.walk(base_address):
    for file in files:
        if (file.startswith("finetune_train")) :
		age_distribution=np.zeros((101),dtype=float)
		dataset = open(base_address+'/'+file,'r')
		sample_number=0
		for line in dataset:
			sample_number+=1
			parsed_line=re.split(' ', line, 1)
			#age=int(re.search(r' \d+', line).group())
			age=int(parsed_line[1]) 
			age_distribution[age]+=1
			#age_array[age].append(parsed_line[0])

		print "Resampled dataset:"
		print file
		print sample_number
		dataset_distribution=age_distribution/sample_number
		kl_divergence=0
		for i in xrange(0,101):
			kl_divergence+=dataset_distribution[i]*np.log((dataset_distribution[i]+1e-10)/(LAP_Validation_distribution[i]+1e-10))
		#print 'kl_divergence of dataset with LAP Validation: '+str(kl_divergence)
		outputfile.write(file+','+str(kl_divergence)+'\n')
		fig, ax = plt.subplots()
		plt.plot(dataset_distribution,'k',LAP_Validation_distribution,'r')
		ax.set_title('whole dataset:black; partial dataset:blue CE:'+str(kl_divergence))
		ax.set_xlabel('Age')
		ax.set_ylabel('Probability')
		plt.show()
		del dataset
		del age_distribution
		del dataset_distribution 		


''''

inputfile = open(Imagelist,'r')
#age_array=np.empty((101,),dtype=np.object_)
#age_array.fill([])
#age_array = np.frompyfunc(list,1,1)(age_array)

age_distribution=np.zeros((101),dtype=int)
#print len(age_array)

sample_number=0
for line in inputfile:
	sample_number+=1
	parsed_line=re.split(' ', line, 1)
	#age=int(re.search(r' \d+', line).group())
	age=int(parsed_line[1]) 
	age_distribution[age]+=1
	#age_array[age].append(parsed_line[0])

print Imagelist
print sample_number



fig, ax = plt.subplots()

plt.plot(age_distribution)

ax.set_xlabel('Age')
ax.set_ylabel('Number of Sample')
#ax.set_title(r'Age distribution of the text file')
ax.set_title(Imagelist)
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()


EstimatedAge=np.asarray(EstimatedAge)
RealAge=np.asarray(RealAge)
MAE=np.average(np.absolute(EstimatedAge- RealAge))
RAA=np.average(RealAge)
EAA=np.average(EstimatedAge)
print 'Mean of Real Age= '+str(RAA)
print 'Mean of Estimated Age= ' + str(EAA)
print 'The mean absolute error= ' +str(MAE)
print 'total test size: '+ str(batch_number)


fig, ax = plt.subplots()
overal_distribution=whole_label/batch_number
partial_distribution=partial_distribution/maximum_predicted_samples
Estimated_distribution=age_plot/maximum_predicted_samples
print 'Sample number:'+str(maximum_predicted_samples)
kl_divergence=0
for i in xrange(0,101):
	kl_divergence+=Estimated_distribution[i]*np.log((Estimated_distribution[i]+1e-10)/(overal_distribution[i]+1e-10))
print 'kl_divergence expected: '+str(kl_divergence)


#plt.plot(age_plot,'k',partial_label,'b')
plt.plot(overal_distribution,'k',partial_distribution,'b',Estimated_distribution,'r')
ax.set_title('whole dataset:black; partial dataset:blue')
ax.set_xlabel('Age')
ax.set_ylabel('Probability')
plt.show()
'''

