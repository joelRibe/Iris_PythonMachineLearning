import math
import numpy as np


def dist_euclidiana_np(v1, v2, index):
    v1 = list(map(float, v1[:index]))
    v2 = list(map(float, v2[:index]))
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)
