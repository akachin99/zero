import numpy as np

class NN_3L_func:

	def __init__(self):
		print("NeuralNetwork 3 Layer()")

	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def identify_function(self, x):
		return x

	def init_network(self):
		self.network = {}
		self.network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
		self.network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
		self.network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
		self.network['B1'] = np.array([0.1, 0.2, 0.3])
		self.network['B2'] = np.array([0.1, 0.2])
		self.network['B3'] = np.array([0.1, 0.2])

		return self.network

	def forward(self, network, x):
#		self.W1, self.W2, self.W3 = network['W1'], network['W2'], network['W3']
		self.W1 = network['W1']
		self.W2 = network['W2']
		self.W3 = network['W3']
#		self.b1, self.b2, self.b3 = network['B1'], network['B2'], network['B3']
		self.b1 = network['B1']
		self.b2 = network['B2']
		self.b3 = network['B3']

		self.a1 = np.dot(x, self.W1) + self.b1
		self.z1 = self.sigmoid(self.a1)
		self.a2 = np.dot(self.z1, self.W2) + self.b2
		self.z2 = self.sigmoid(self.a2)
		self.a3 = np.dot(self.z2, self.W3) + self.b3
		self.y = self.identify_function(self.a3)

		return self.y
