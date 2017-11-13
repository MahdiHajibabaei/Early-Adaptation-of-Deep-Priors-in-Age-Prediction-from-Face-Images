#!/usr/bin/env sh
set -e

./build/tools/caffe train -solver /srv/glusterfs/hmahdi/IMDB/models/training_scripts/1_vgg_m1_fgnet_chalearn_solver.prototxt -snapshot /srv/glusterfs/hmahdi/IMDB/models/snapshots/imdb_finetunes_LAP_matched_iter_225000.solverstate  $@
