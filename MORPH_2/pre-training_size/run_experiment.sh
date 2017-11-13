#!/usr/bin/env sh
set -e

#Pre-training with only 100 samples from IMDB dataset
#./build/tools/caffe train -solver /srv/glusterfs/hmahdi/IMDB/models/smaller_pretraining/100/LAP_100_solver.prototxt -weights /srv/glusterfs/hmahdi/IMDB/models/vgg_m1_wiki_imdb_equal_iter_500000.caffemodel  $@

#Pre-training with only 1000 samples from IMDB dataset
#./build/tools/caffe train -solver /srv/glusterfs/hmahdi/IMDB/models/smaller_pretraining/1000/LAP_1000_solver.prototxt -weights /srv/glusterfs/hmahdi/IMDB/models/vgg_m1_wiki_imdb_equal_iter_500000.caffemodel  $@

#Pre-training with only 10000 samples from IMDB dataset
./build/tools/caffe train -solver /srv/glusterfs/hmahdi/IMDB/models/smaller_pretraining/10000/LAP_10000_solver.prototxt -weights /srv/glusterfs/hmahdi/IMDB/models/vgg_m1_wiki_imdb_equal_iter_500000.caffemodel  $@
