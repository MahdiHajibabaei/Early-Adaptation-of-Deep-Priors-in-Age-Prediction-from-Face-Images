#!/usr/bin/env sh
set -e

./build/tools/caffe train -solver /srv/glusterfs/hmahdi/IMDB/models/training_scripts/1_vgg_m1_fgnet_chalearn_solver.prototxt -weights /srv/glusterfs/hmahdi/IMDB/models/vgg_m1_wiki_imdb_equal_iter_500000.caffemodel  $@
