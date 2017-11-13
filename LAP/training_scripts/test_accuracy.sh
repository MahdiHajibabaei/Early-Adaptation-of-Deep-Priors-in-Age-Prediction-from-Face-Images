#!/usr/bin/env sh
set -e

#./build/tools/caffe test --model=/srv/glusterfs/hmahdi/IMDB/models/training_scripts/1_vgg_m1_fgnet_chalearn_test.prototxt --weights=/srv/glusterfs/hmahdi/IMDB/models/snapshots/imdb_finetunes_LAP_matched_iter_225000.caffemodel  -stage=test-on-test --iterations=1136 $@

#./build/tools/caffe test --model=/srv/glusterfs/hmahdi/IMDB/models/training_scripts/1_vgg_m1_fgnet_chalearn_test.prototxt --weights=/scratch_net/biwidl09/hmahdi/IMDB/datas/models/vgg_m1_chalearn_1_imdb_uniform_iter_10000.caffemodel  -stage=test-on-test --iterations=1136 $@

./build/tools/caffe test --model=/srv/glusterfs/hmahdi/IMDB/models/training_scripts/1_vgg_m1_fgnet_chalearn_test.prototxt --weights=/scratch_net/biwidl09/hmahdi/IMDB/datas/models/vgg_m1_chalearn_1_imdb_uniform_4p_iter_500.caffemodel  -stage=test-on-test --iterations=1136 $@

