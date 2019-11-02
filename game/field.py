import copy
import numpy as np

class closedField:
	def __init__(self, other=None, size=None):
		if other:
			self.field = copy.deepcopy(other.field)
		elif size:
			self.field = np.zeros(size, dtype=bool)
		else:
			raise Exception

	def __getitem__(self, ind):
		return self.field[ind, :]

	def __eq__(self, other):
		return np.array_equal(self.field, other.field)

	def NextStep(self):
		shape = self.field.shape
		self.prev_field = copy.deepcopy(self.field)
		self.field = np.zeros(shape, dtype=bool)

		def count_state(field, i, j):
			neighbours_alive = 0

			if i > 0:
				if j > 0:
					neighbours_alive += field[i - 1][j - 1]
				neighbours_alive += field[i - 1][j]
				if j < shape[1] - 1:
					neighbours_alive += field[i - 1][j + 1]
			if j > 0:
				neighbours_alive += field[i][j - 1]
			if j < shape[1] - 1:
				neighbours_alive += field[i][j + 1]
			if i < shape[0] - 1:
				if j > 0:
					neighbours_alive += field[i + 1][j - 1]
				neighbours_alive += field[i + 1][j]
				if j < shape[1] - 1:
					neighbours_alive += field[i + 1][j + 1]

			if field[i][j] == False: 
				if neighbours_alive == 3:
					return True
				else:
					return False

			if field[i][j] == True:
				if neighbours_alive == 2 or neighbours_alive == 3:
					return True
				else:
					return False

		for i in range(shape[0]):
			for j in range(shape[1]):
				self.field[i][j] = count_state(self.prev_field, i, j)

		return self.field

	def GetPrevField(self):
		return self.prev_field

	def GetField(self):
		return self.field

	def GetShape(self):
		return self.field.shape
