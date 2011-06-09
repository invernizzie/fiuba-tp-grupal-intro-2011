from unittest import TestSuite
import unittest

from t_dijkstra import TestDijkstra
from t_graph import TestGraph
from test.t_ip import TestIp
from test.t_router import TestRouter

test_modules = [ TestGraph, TestDijkstra, TestIp, TestRouter] 
test_suite = TestSuite()

for test in test_modules:
    t = unittest.TestLoader().loadTestsFromTestCase(test)
    test_suite.addTest(t)
