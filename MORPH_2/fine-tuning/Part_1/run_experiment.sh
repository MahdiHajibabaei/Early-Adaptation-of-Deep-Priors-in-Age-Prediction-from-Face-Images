##This script runs a full adaptation experiments using the pre-trained weight in weight_path on either 3 of the clusters
#!/usr/bin/env sh
set -e
# This script first creates the solver files for training and then run the trainings one by one in the loop and tests and writes the MAE scores in a CSV since the Caffe does not allow us to change the File name of caffe model in the training stage
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/IMDB-Wiki/imdb-wiki_0.00_iter_000.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/IMDB_Original/imdb-original_0.00_iter_000.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/IMDB_Uniform/imdb-uniform_0.00_iter_000.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/MORPH_Matched/MORPH_Matched_iter_250000.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/ImageNet/VGG_ILSVRC_16_layers.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/vgg_face_caffe/VGG_FACE.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/MORPH_100/imdb_MORPH_Matched_100_iter_68.caffemodel
#weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/MORPH_1000/imdb_MORPH_Matched_1000_iter_678.caffemodel
weight_path=/srv/glusterfs/hmahdi/IMDB/morph_target/MORPH_10000/imdb_MORPH_Matched_10000_iter_6783.caffemodel


for  solver_path in /home/hmahdi/caffe/examples/morph/fine-tuning/Learning_curve_prototxts_1/DEX_solver_*
do 
	echo $solver_path
	./build/tools/caffe train -solver ${solver_path} -weights ${weight_path}  $@	
done



