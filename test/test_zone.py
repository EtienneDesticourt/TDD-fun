import unittest
from app.Zone import Zone
from math import hypot
import numpy

class ZoneTestCase(unittest.TestCase):

    def test_zone_collidelist_no_collision(self):
        Zone1 = Zone((0, 0), (10, 4))
        Zone2 = Zone((0, 0), (3, 10))
        Zone3 = Zone((0, 6), (10, 4))
        Zone4 = Zone((4, 0), (6, 10))

        Zone5 = Zone((3, 4), (1,2))

        result = Zone5.collidelist([Zone1, Zone2, Zone3, Zone4])
        assert isinstance(result, bool)
        assert result == False

    def test_zone_collidelist_collision(self):
        Zone1 = Zone((0, 0), (10, 4))
        Zone2 = Zone((0, 0), (3, 10))
        Zone3 = Zone((0, 6), (10, 4))
        Zone4 = Zone((4, 0), (6, 10))

        Zone5 = Zone((3, 4), (1,2))

        result = Zone1.collidelist([Zone2, Zone3, Zone4])
        assert isinstance(result, bool)
        assert result == True

    def test_zone_add_zone(self):
        Zone1 = Zone((1,2), (1,1))
        Zone2 = Zone((3,4), (5,6))

        Zone3 = Zone1 + Zone2
        assert isinstance(Zone3, Zone)
        assert Zone3.x == 4
        assert Zone3.y == 6
        assert Zone1.x == 1
        assert Zone1.y == 2
        assert Zone2.x == 3
        assert Zone2.y == 4

    def test_zone_add_ip_zone(self):
        Zone1 = Zone((1,2), (1,1))
        Zone2 = Zone((3,4), (5,6))

        Zone2 += Zone1
        assert isinstance(Zone2, Zone)
        assert Zone2.x == 4
        assert Zone2.y == 6
        assert Zone1.x == 1
        assert Zone1.y == 2

    def test_zone_truediv(self):        
        Zone1 = Zone((8,3), (1,1))

        result = Zone1 / 2
        assert isinstance(result, Zone)
        assert result.x == 4
        self.assertAlmostEqual(result.y, 1.5)

    def test_zone_floordiv(self):
        Zone1 = Zone((8,3), (1,1))

        result = Zone1 // 2
        assert isinstance(result, Zone)
        assert result.x == 4
        assert result.y == 1

    def test_zone_sub(self):
        Zone1 = Zone((1,2), (1,1))
        Zone2 = Zone((3,5), (5,6))

        Zone3 = Zone2 - Zone1
        assert isinstance(Zone3, Zone)
        assert Zone3.x == 2
        assert Zone3.y == 3
        assert Zone1.x == 1
        assert Zone1.y == 2
        assert Zone2.x == 3
        assert Zone2.y == 5

    def test_zone_normalize(self):
        Zone1 = Zone((1, 2), (1,1))
        distance = hypot(1, 2)
        x = 1 / distance 
        y = 2 / distance

        Actual = Zone1.normalize()
        assert isinstance(Actual, Zone)
        self.assertAlmostEqual(Actual.x, x)
        self.assertAlmostEqual(Actual.y, y)

    def test_zone_square(self):
        Zone1 = Zone((4, 5), (1,1))
        
        Actual = Zone1.square()
        assert isinstance(Actual, Zone)
        assert Actual.x == 16
        assert Actual.y == 25

    def test_zone_sum(self):
        Zone1 = Zone((4, 5), (1,1))
        
        actual = Zone1.sum()
        assert isinstance(actual, numpy.float32)
        assert actual == 9

    def test_zone_neg(self):
        Zone1 = Zone((4, 5), (1,1))
        
        Actual = -Zone1
        assert isinstance(Actual, Zone)
        assert Actual.x == -4
        assert Actual.y == -5





        
        