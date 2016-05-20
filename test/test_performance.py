import unittest
import numpy as np
from app.Zone import Zone
from app.Flocker import Flocker
import time

class PerformanceTestCase(unittest.TestCase):

    def test_performance_flocker(self):
    	total = 0
    	numRuns = 10
    	maxNumUnits = 400
    	maxSizeFlock = 20

    	units = []
    	for u in range(maxNumUnits):
    		fl = Flocker(Zone((3,4), (5,6)))
    		fl.speed = np.array([4.3, 5.2], dtype=np.float32)
    		curFlock = []
    		for f in range(maxSizeFlock):
    			ofl = Flocker(Zone((4,5), (5,6)))
    			ofl.speed = np.array([6.7,7.8], dtype=np.float32)
    			curFlock.append(ofl)
    		fl.Flock = curFlock
    		units.append(fl)

    	for r in range(numRuns):
    		start = time.time()
    		for u in units:
    			t = u.cohere()
    			t = u.separate()
    			t = u.align()
    		end = time.time()
    		total += end - start

    	assert total / numRuns <= 0.1


        
        