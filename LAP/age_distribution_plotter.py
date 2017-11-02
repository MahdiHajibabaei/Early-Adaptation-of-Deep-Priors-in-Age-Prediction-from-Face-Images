
# This script parses a txt file of a dataset with labels that is normally fed to Caffe for training and plots the age distribution of it

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re

Imagelist='/srv/glusterfs/hmahdi/IMDB/morph_target/Pre-training_sizes/10000/MORPH_matched_10000_training_set.txt'

inputfile = open(Imagelist,'r')
age_array=np.empty((101,),dtype=np.object_)
age_array.fill([])
age_array = np.frompyfunc(list,1,1)(age_array)

age_distribution=np.zeros((101),dtype=int)
print len(age_array)

sample_number=0
for line in inputfile:
	sample_number+=1
	parsed_line=re.split(' ', line, 1)
	#age=int(re.search(r' \d+', line).group())
	age=int(parsed_line[1]) 
	age_distribution[age]+=1
	age_array[age].append(parsed_line[0])

print sample_number



fig, ax = plt.subplots()

plt.plot(age_distribution)

ax.set_xlabel('Age')
ax.set_ylabel('Number of Sample')
#ax.set_title(r'Age distribution of the text file')
#ax.set_title(Imagelist)
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()

