import unittest
from app.Character import Character
from app.Zone import Zone
from app.Flocker import Flocker
from math import sqrt, hypot
import numpy as np

class FlockerTestCase(unittest.TestCase):

    def test_flocker_cohere(self):
    	Char1 = Character(strength = 10, life = 10, affiliation = 0, Zone = Zone((1, 2), (1, 1)))
    	Char2 = Character(strength = 10, life = 10, affiliation = 0, Zone = Zone((3, 4), (1, 1)))
    	flock = [Char1, Char2]

    	Flocker1 = Flocker(Zone((4, 6), (1, 1)))
    	Flocker1.Flock = flock

    	x = 4 / 2 - 4
    	y = 6 / 2 - 6
    	dist = hypot(x, y)
    	x, y = (x / dist, y / dist)

    	result = Flocker1.cohere()
    	self.assertAlmostEqual(result[0], x)
    	self.assertAlmostEqual(result[1], y)

    	Flocker1.Flock = []
    	actual = Flocker1.cohere()
    	assert actual[0] == 0
    	assert actual[1] == 0

    def test_flocker_separate(self):     	
    	Char1 = Character(strength = 10, life = 10, affiliation = 0, Zone = Zone((1, 2), (1, 1)))
    	Char2 = Character(strength = 10, life = 10, affiliation = 0, Zone = Zone((3, 4), (1, 1)))
    	flock = [Char1, Char2]

    	Flocker1 = Flocker(Zone((5, 6), (1, 1)))
    	Flocker1.Flock = flock


    	offset1 = (-4 / 32, -4 / 32)
    	offset2 = (-2 / 8, -2 / 8)
    	steering = (- offset1[0] - offset2[0], -offset1[0] -offset2[0])
    	length = hypot(steering[0], steering[1])
    	steering = (steering[0] / length, steering[1] / length)


    	actual = Flocker1.separate()
    	self.assertAlmostEqual(actual[0], steering[0])
    	self.assertAlmostEqual(actual[0], steering[1])

    	Flocker1.Flock = []
    	actual = Flocker1.separate()
    	assert actual[0] == 0
    	assert actual[1] == 0

    def test_flocker_align(self):
    	Flocker1 = Flocker(Zone((0,0), (1, 1)))
    	Flocker1.speed = np.array([1, 2], dtype=np.float32)
    	Flocker2 = Flocker(Zone((0,0), (1, 1)))
    	Flocker1.speed = np.array([3, 4], dtype=np.float32)

    	flock = [Flocker1, Flocker2]

    	Flocker3 = Flocker(Zone((0, 0), (1, 1)))
    	Flocker3.speed = np.array([5, 6], dtype=np.float32)
    	Flocker3.Flock = flock

    	steering = (Flocker1.speed + Flocker2.speed)
    	steering = (steering / 2 - Flocker3.speed)
    	steering = steering / hypot(*steering)

    	actual = Flocker3.align()
    	assert actual[0] == steering[0]
    	assert actual[1] == steering[1]

    	Flocker3.Flock = []
    	actual = Flocker3.align()
    	assert actual[0] == 0
    	assert actual[1] == 0    	

    def test_flock_seek(self):
    	Flocker1 = Flocker(Zone((3, 4), (1, 1)))
    	Flocker1.speed = np.array([5, 6], dtype=np.float32)
    	Flocker2 = Flocker(Zone((1, 5), (1, 1)))

    	actual = Flocker1.seek(Flocker2.Zone.position)
    	assert actual[0] == -7 #(1 - 3) - 5
    	assert actual[1] == -5 #(5 - 4) - 6

#     def test_flock_avoid(self):
#     	assert True

#     def test_flock_queue(self):
#     	assert True



        