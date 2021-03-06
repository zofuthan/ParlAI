# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
# Download and build the data if it does not exist.

import parlai.core.build_data as build_data
import os


def build(opt):
    dpath = os.path.join(opt['datapath'], 'SQuAD')

    if not build_data.built(dpath):
        print('[building data: ' + dpath + ']')
        build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        fname1 = 'train-v1.1.json'
        fname2 = 'dev-v1.1.json'
        url = 'https://rajpurkar.github.io/SQuAD-explorer/dataset/'
        build_data.download(dpath, url + fname1)
        build_data.download(dpath, url + fname2)

        # Mark the data as built.
        build_data.mark_done(dpath)
