import numpy as np
import matplotlib.pylab as plt

class Step_Function:

	def __init__(self):
		print("step_function(np.array)")

	def step_function(self, x):
		self.x = x
		self.y = np.array(x > 0, dtype = np.int)
		return self.y

	def draw_graph(self):
		plt.plot(self.x, self.y)
		plt.ylim(-0.1, 1.1)
		plt.show()
		return
