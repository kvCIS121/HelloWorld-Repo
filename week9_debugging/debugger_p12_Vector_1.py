from math import sqrt
class Vector:
	def __init__(self, x_direction, y_direction):
		self._x_direction = x_direction
		self._y_direction = y_direction
	
	def get_x_direction(self):
		return self._x_direction
	
	def set_x_direction(self, x_direction):
		self._x_direction = x_direction
	
	def get_y_direction(self):
		return self._y_direction
	
	def set_y_direction(self, y_direction):
		self._y_direction = y_direction
	
	def get_magnitude(self):
		magnitude = sqrt(self._x_direction ** 2 + self._y_direction ** 2)
		return magnitude
	

# Test the class with a sample input
vector = Vector(3, 4)
print(vector.get_x_direction())	# Expected output: 3
print(vector.get_y_direction())	# Expected output: 4
print(vector.get_magnitude())	# Expected output: 5.0
vector.set_x_direction(6)
print(vector.get_x_direction())	# Expected output: 6
vector.set_y_direction(8)
print(vector.get_y_direction())	# Expected output: 8
print(vector.get_magnitude())	# Expected output: 10.0