class LogicCircuit:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        print("Input AND(x1, x2) or OR or NAND!!")

#    def CommonCul(x1, x2, w1, w2, theta):
#        tmp = x1 * w1 + x2 * w2
#        if tmp > theta:
#            return 1
#        else:
#            return 0

    def AND(self):
        w1 = 1
        w2 = 1
        theta = 1
        tmp = self.x1 * w1 + self.x2 * w2
        if tmp > theta:
            print("1")
        else:
            print("0")
        #result = CommonCul(x1, x2, w1, w2, theta)
        #return relsult

    def OR(self):
#        w1, w2, theta = 1, 1, 0
        self.w1 = 1
        self.w2 = 1
        self.theta = 0
        self.tmp = self.x1 * self.w1 + self.x2 * self.w2
        if self.tmp > self.theta:
            return 1
        else:
            return 0
        #result = CommonCul(x1, x2, w1, w2, theta)
        #return relsult
