import numpy
from math import hypot

class Zone(object):
	def __init__(self, coords, size):
		self.position = numpy.array(coords, dtype=numpy.float32)
		self.size = numpy.array(size, dtype=numpy.float32)

	def collidelist(self, Zones):
		for OtherZone in Zones:
			w = 0.5 * (self.w + OtherZone.w);
			h = 0.5 * (self.h + OtherZone.h);
			dx = self.cx - OtherZone.cx;
			dy = self.cy - OtherZone.cy;
			if abs(dx) < w and abs(dy) < h:
				return True
		return False

	def move_ip(self, offsetX, offsetY):
		self.position += numpy.array([offsetX, offsetY])

	@property 
	def x(self):
		return self.position[0]

	@property
	def y(self):
		return self.position[1]

	@property
	def cx(self):
		return self.x + self.w / 2

	@property
	def cy(self):
		return self.y + self.h / 2

	@property
	def w(self):
		return self.size[0]

	@property 
	def h(self):
		return self.size[1]

	def __add__(self, OtherZone):
		return Zone((OtherZone.x + self.x, OtherZone.y + self.y), (self.w, self.h) )

	def __iadd__(self, OtherZone):
		self.move_ip(OtherZone.x, OtherZone.y)
		return self

	def __truediv__(self, value):
		x = self.x / value
		y = self.y / value
		return Zone((x, y), (self.w, self.h))		

	def __floordiv__(self, value):
		x = self.x // value
		y = self.y // value
		return Zone((x, y), (self.w, self.h))

	def __sub__(self, OtherZone):
		return Zone((self.x - OtherZone.x, self.y - OtherZone.y), (self.w, self.y))

	def __neg__(self):
		return Zone((-self.x, -self.y), (self.w, self.h))

	def normalize(self):
		distance = hypot(self.x, self.y)
		return self / distance

	def square(self):
		return Zone((self.x*self.x, self.y*self.y), (self.w, self.h))

	def sum(self):
		return self.x + self.y
