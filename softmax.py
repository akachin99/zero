import numpy as np

class Softmax:

	def __init__(self):
		print("softmax")

	def softmax(self, a):
		self.exp_a = np.exp(a)
		self.sum_exp_a = np.sum(self.exp_a)
		y = self.exp_a / self.sum_exp_a
		return y

	def softmax2(self, a):
		self.c = np.max(a)
		print(self.c)
		self.exp_a = np.exp(a - self.c)
		print(a - self.c)
		self.sum_exp_a = np.sum(self.exp_a)
		y = self.exp_a / self.sum_exp_a
		return y
