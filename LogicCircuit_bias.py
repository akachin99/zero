
import numpy as np

class LogicCircuit_b:

    def __init__(self):
        print("Input AND(x1, x2) or OR or NAND!")

    def CommonCul(self, x, w, b):
        tmp = np.sum(x * w) + b
        if tmp > 0:
            return 1
        else:
            return 0

    def AND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([1, 1])
        b = -1
        result = self.CommonCul(x, w, b)
        return result

    def OR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([1, 1])
        b = 0
        result = self.CommonCul(x, w, b)
        return result

    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-1, -1])
        b = 2
        result = self.CommonCul(x, w, b)
        return result

    def NOR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-1, -1])
        b = 1
        result = self.CommonCul(x, w, b)
        return result

    def XOR(self, x1, x2):
        s1 = self.NAND(x1, x2)
        s2 = self.OR(x1, x2)
        result = self.AND(s1, s2)
        return result
