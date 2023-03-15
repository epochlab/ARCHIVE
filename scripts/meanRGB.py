#!/usr/bin/env python3

import os
import numpy as np
from PIL import Image

def load(x):
    return Image.open(x)

def reformat(x, res):
    if x.size[0] > x.size[1]:
        align = 'portraint'
        factor = x.size[1] / res[0]
        reformat_img = x.resize(x.size[0]/factor, res[1])
    elif x.size[0] < x.size[1]:
        align = 'landscape'
        factor = x.size[0] / res[0]
        reformat_img = x.resize(res[0], int(x.size[1]/factor))
    else:
        align = 'square'
        reformat_img = x.resize((res[0], res[1]))

    if align != 'square':
        reformat_img = reformat_img.crop(0, res[1], res[0], 0)

    return reformat_img

def meanrgb(dataset, res):
    array = np.zeros(res, dtype='float32')

    for fid, file in enumerate(dataset):
        instance = reformat(load(file), IMAGE_SHAPE)
        array += np.array(instance)

    return array / len(dataset)

ROOT = 'path_to_directory'
IMAGE_SHAPE = (256,256,3)

dataset = []
for path, subdirs, files in os.walk(ROOT):
    for name in files:
        filepath = os.path.join(path, name)
        dataset.append(filepath)

mean_array = meanrgb(dataset, IMAGE_SHAPE)
Image.fromarray(np.uint8(mean_array)).save('sample.png')
