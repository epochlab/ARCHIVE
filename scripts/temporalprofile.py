#!/usr/bin/env python3

import os
import numpy as np
from PIL import Image

def temporalprofile(x, w_point):
    sequence = sorted(os.listdir(x))
    p_length = len(sequence)

    first_frame = Image.open(x + "/" + sequence[0])
    height = np.array(first_frame).shape[0]

    profile = np.zeros(shape = (p_length, height, 3))

    i = 0
    for image in sequence:
        frame = Image.open(os.path.join(x, image))
        frame = np.array(frame)

        line = frame[:,w_point,:]
        profile[i,:,:] = line

        i += 1

    profile = Image.fromarray(profile.astype(np.uint8))
    profile.save("temporalprofile.png")
    print("Profile cached")
