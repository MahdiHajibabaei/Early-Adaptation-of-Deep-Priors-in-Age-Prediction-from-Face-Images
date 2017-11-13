#!/usr/bin/env sh
set -e
# This script goes through all solver prototxts within one folder, trains a CNN with weights of the network given in weight_path as starting point and stores the resulting CNN to the directory specified in solvers files

weight_path=/srv/glusterfs/hmahdi/IMDB/models/smaller_pretraining_snapshots/imdb_LAP_Matched_10000_iter_6783.caffemodel


for  solver_path in /home/hmahdi/caffe/examples/imdb/Pre-training_distribution/Learning_curve_prototxts_2/DEX_solver_*
do 
	echo $solver_path
	./build/tools/caffe train -solver ${solver_path} -weights ${weight_path}  $@	
done



