class LogicCircuit2:
    def __init__(self):
        print("Input AND(x1, x2) or OR or NAND!")

    def CommonCul(self, x1, x2, w1, w2, theta):
        tmp = x1 * w1 + x2 * w2
        if tmp > theta:
            return 1
        else:
            return 0

    def AND(self, x1, x2):
        w1, w2, theta = 1, 1, 1
        result = self.CommonCul(x1, x2, w1, w2, theta)
        return result

    def OR(self, x1, x2):
        w1, w2, theta = 1, 1, 0
        result = self.CommonCul(x1, x2, w1, w2, theta)
        return result

    def NAND(self, x1, x2):
        w1, w2, theta = -1, -1, -2
        result = self.CommonCul(x1, x2, w1, w2, theta)
        return result

    def NOR(self, x1, x2):
        w1, w2, theta = -1, -1, -1
        result = self.CommonCul(x1, x2, w1, w2, theta)
        return result

    def XOR(self, x1, x2):
        s1 = self.NAND(x1, x2)
        s2 = self.OR(x1, x2)
        result = self.AND(s1, s2)
        return result
