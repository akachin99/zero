
import numpy as np

class step_function:

    def __init__(self):
        print("Input np.array ")

    def step_func(self, x):
        y = x > 0
        return y.astype(np.int)