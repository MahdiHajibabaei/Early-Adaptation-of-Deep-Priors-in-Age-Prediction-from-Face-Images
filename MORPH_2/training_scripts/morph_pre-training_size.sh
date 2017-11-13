## This script will schedule pre-training with MORPH2 matched datasets of different sizes 
#!/bin/bash
#
## otherwise the default shell would be used
#$ -S /bin/bash
#
## <= 1h is short queue, <= 6h is middle queue, <= 48 h is long queue
#$ -l h_rt=6:00:00
 
## the maximum memory usage of this job, (below 4G does not make much sense)
#$ -l h_vmem=24G
#$ -l gpu=3
 
## stderr and stdout are merged together to stdout
#$ -j y
#,4
# logging directory. preferrably on your scratch
#$ -o ~/caffe/examples/morph/pre-training_size/Logs/morph_matched_pretraining_sizes.txt
#
## send mail on job's end and abort
## -m a

# if you need to export custom libs, you can do that here
#export LD_LIBRARY_PATH=/scratch_net/yourhost/yourname/lib/opencv/lib:$LD_LIBRARY_PATH
 
# call your calculation executable, redirect output
echo $SGE_GPU
cd caffe
echo $(pwd)
echo $LD_LIBRARY_PATH
source setpath.sh

/srv/glusterfs/hmahdi/IMDB/morph_target/Pre-training_sizes/run_experiment.sh -gpu  $SGE_GPU
