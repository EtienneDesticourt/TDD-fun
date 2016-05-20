from math import hypot
from app.Zone import Zone
import numpy as np

class Flocker(object):
	def __init__(self, Zone):
		self.Zone = Zone
		self.Flock = []
		self.speed = np.array([0,0], dtype=np.float32)

	def seek(self, targetPosition):
		return (targetPosition - self.Zone.position) - self.speed

	def cohere(self):
		steering = np.array([0,0], dtype=np.float32)
		if len(self.Flock) == 0: return steering

		for buddy in self.Flock:
			steering += buddy.Zone.position

		steering = steering / len(self.Flock) - self.Zone.position
		return steering / np.linalg.norm(steering)

	def separate(self):
		steering = np.array([0,0], dtype=np.float32)
		if len(self.Flock) == 0: return steering

		for buddy in self.Flock:
			offset = buddy.Zone.position - self.Zone.position
			lengthSquared = offset.dot(offset)
			steering += - offset / lengthSquared

		return steering / np.linalg.norm(steering)

	def align(self):
		steering = np.array([0,0], dtype=np.float32)
		if len(self.Flock) == 0: return steering

		for FlockMate in self.Flock:
			steering += FlockMate.speed

		steering = (steering / len(self.Flock) - self.speed)
		steering = steering / hypot(*steering)
		return steering
