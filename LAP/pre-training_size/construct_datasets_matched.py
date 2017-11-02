
# This script is supposed to take a txt list of the dataset, with the age labels included, and after parsing the whole file and putting the samples
# with the same age in the same bucket, another txt file is fed to the script and the distribution of this new  dataset should be applied to the former
# dataset to construct a new dataset

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re
from random import shuffle
import pickle

# The main source dataset whose data is used for training
Imagelist='/srv/glusterfs/hmahdi/IMDB/models/datasets/shuffled_test_set.txt'
inputfile = open(Imagelist,'r')
# The array of lists that would be filled with the directory of images
IMDB_age_array=np.empty((101,),dtype=np.object_)
IMDB_age_array.fill([])
IMDB_age_array = np.frompyfunc(list,1,1)(IMDB_age_array)
# The array that will keep the number of entries in each age group
IMDB_age_distribution=np.zeros((101),dtype=int)
#print len(age_array)

IMDB_sample_number=0
for line in inputfile:
	IMDB_sample_number+=1
	parsed_line=re.split(' ', line, 1)
	age=int(parsed_line[1]) 
	IMDB_age_distribution[age]+=1
	IMDB_age_array[age].append(parsed_line[0]+' '+str(age))

print  IMDB_sample_number
fig, ax = plt.subplots()

plt.plot(IMDB_age_distribution)
''''
ax.set_xlabel('Age')
ax.set_ylabel('Number of Sample')
#ax.set_title(r'Age distribution of the text file')
#ax.set_title(Imagelist)
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
'''


# The secondary source dataset whose distribution is used for training
Imagelist='/home/hmahdi/caffe/examples/imdb/imdbwiki-0-101_1_test.txt'
inputfile = open(Imagelist,'r')
age_array=np.empty((101,),dtype=np.object_)
age_array.fill([])
age_array = np.frompyfunc(list,1,1)(age_array)

LAP_age_distribution=np.zeros((101),dtype=int)
#print len(age_array)

LAP_sample_number=0
for line in inputfile:
	LAP_sample_number+=1
	parsed_line=re.split(' ', line, 1)
	#age=int(re.search(r' \d+', line).group())
	age=int(parsed_line[1]) 
	LAP_age_distribution[age]+=1
	#age_array[age].append(parsed_line[0]+' '+str(age))

print LAP_sample_number
'''
plt.plot(LAP_age_distribution)

ax.set_xlabel('Age')
ax.set_ylabel('Number of Sample')
#ax.set_title(r'Age distribution of the text file')
ax.set_title(Imagelist)
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
'''
#Reduction_ratio=0.0003
#Reduction_ratio=0.000343# for training 100 samples
#Reduction_ratio=0.00072# for validation 13 samples
Reduction_ratio=0.02725# for 10000 samples
# This scale is used for resampling from IMDB
resampling_scale = Reduction_ratio * IMDB_sample_number/LAP_sample_number
print resampling_scale

redistributed_age=[]
# just for making sure we use as many novel samples as possible
for age in xrange(0,101):
	if (LAP_age_distribution[age])>0:
		provided_samples=IMDB_age_distribution[age]
		required_samples=int(LAP_age_distribution[age]*resampling_scale)
		if (required_samples>provided_samples):
			redistributed_age.extend(np.random.choice(IMDB_age_array[age],size=provided_samples,replace=False))
			redistributed_age.extend(np.random.choice(IMDB_age_array[age],size=required_samples-provided_samples,replace=True))
		else :
			redistributed_age.extend(np.random.choice(IMDB_age_array[age],size=required_samples,replace=False))

print len(redistributed_age)
base_address=''
dataset = open(base_address+'LAP_matched_10000_test_set.txt','w+')
shuffle(redistributed_age)
for item in redistributed_age:
 	dataset.write("%s\n" % item)
''''
fig, ax = plt.subplots()

plt.plot(age_distribution)

ax.set_xlabel('Age')
ax.set_ylabel('Number of Sample')
#ax.set_title(r'Age distribution of the text file')
ax.set_title(Imagelist)
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
'''
