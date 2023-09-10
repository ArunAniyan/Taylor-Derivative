## Taylor Derivative methods

import numpy as np


def diff(array):
    midval = array[1, 1]
    array = array - midval
    return np.sum(array) / 8


def grad(input, kernel_size=3, stride=1):
    dimx, dimy = input.shape
    for i in range(0, dimx - kernel_size + 1):
        for j in range(dimy):
            continue


if "__name__" == "__main__":
    diff([1, 2, 3])
