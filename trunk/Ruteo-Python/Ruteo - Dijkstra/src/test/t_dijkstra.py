import unittest
from graph import Graph
from dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    
    def setUp(self):
        self.g = Graph()
        self.g.add_vertex('1')
        self.g.add_vertex('2')
        self.g.add_vertex('3')
        self.g.add_vertex('4')
        self.g.add_vertex('5')
        self.g.add_vertex('6')
        
        self.g.add_edge('1', '2', 7)
        self.g.add_edge('1', '3', 9)
        self.g.add_edge('1', '6', 14)
        self.g.add_edge('2', '3', 10)
        self.g.add_edge('2', '4', 15)
        self.g.add_edge('3', '4', 11)
        self.g.add_edge('3', '6', 2)
        self.g.add_edge('4', '5', 6)
        self.g.add_edge('5', '6', 9)

    def tearDown(self):
        self.g = None
        
    def test_min_paths(self):
        d = Dijkstra(self.g)
        paths = d.execute()[0]
        
        self.assertEqual(paths[('1', '2')], ['1', '2'])
        self.assertEqual(paths[('1', '3')], ['1', '3'])
        self.assertEqual(paths[('1', '4')], ['1', '3', '4'])
        self.assertEqual(paths[('1', '5')], ['1', '3', '6', '5'])
        self.assertEqual(paths[('1', '6')], ['1', '3', '6'])

        self.assertEqual(paths[('2', '1')], ['2', '1'])
        self.assertEqual(paths[('2', '3')], ['2', '3'])
        self.assertEqual(paths[('2', '4')], ['2', '4'])
        self.assertEqual(paths[('2', '5')], ['2', '3', '6', '5'])
        self.assertEqual(paths[('2', '6')], ['2', '3', '6'])
        
        self.assertEqual(paths[('3', '1')], ['3', '1'])
        self.assertEqual(paths[('3', '2')], ['3', '2'])
        self.assertEqual(paths[('3', '4')], ['3', '4'])
        self.assertEqual(paths[('3', '5')], ['3', '6', '5'])
        self.assertEqual(paths[('3', '6')], ['3', '6'])
        
        self.assertEqual(paths[('4', '1')], ['4', '3', '1'])
        self.assertEqual(paths[('4', '2')], ['4', '2'])
        self.assertEqual(paths[('4', '3')], ['4', '3'])
        self.assertEqual(paths[('4', '5')], ['4', '5'])
        self.assertEqual(paths[('4', '6')], ['4', '3','6'])
        
        self.assertEqual(paths[('5', '1')], ['5', '6', '3', '1'])
        self.assertEqual(paths[('5', '2')], ['5', '4', '2'])
        self.assertEqual(paths[('5', '3')], ['5', '6', '3'])
        self.assertEqual(paths[('5', '4')], ['5', '4'])
        self.assertEqual(paths[('5', '6')], ['5', '6'])
        
        self.assertEqual(paths[('6', '1')], ['6', '3', '1'])
        self.assertEqual(paths[('6', '2')], ['6', '3', '2'])
        self.assertEqual(paths[('6', '3')], ['6', '3'])
        self.assertEqual(paths[('6', '4')], ['6', '3', '4'])
        self.assertEqual(paths[('6', '5')], ['6', '5'])
        
    def test_distance(self):
        d = Dijkstra(self.g)
        distances = d.execute()[1]
        
        self.assertEqual(distances[('1', '2')], 7)
        self.assertEqual(distances[('1', '3')], 9)
        self.assertEqual(distances[('1', '4')], 20)
        self.assertEqual(distances[('1', '5')], 20)
        self.assertEqual(distances[('1', '6')], 11)
        
        self.assertEqual(distances[('2', '1')], 7)
        self.assertEqual(distances[('2', '3')], 10)
        self.assertEqual(distances[('2', '4')], 15)
        self.assertEqual(distances[('2', '5')], 21)
        self.assertEqual(distances[('2', '6')], 12)
        
        self.assertEqual(distances[('3', '1')], 9)
        self.assertEqual(distances[('3', '2')], 10)
        self.assertEqual(distances[('3', '4')], 11)
        self.assertEqual(distances[('3', '5')], 11)
        self.assertEqual(distances[('3', '6')], 2)
        
        self.assertEqual(distances[('4', '1')], 20)
        self.assertEqual(distances[('4', '2')], 15)
        self.assertEqual(distances[('4', '3')], 11)
        self.assertEqual(distances[('4', '5')], 6)
        self.assertEqual(distances[('4', '6')], 13)
        
        self.assertEqual(distances[('5', '1')], 20)
        self.assertEqual(distances[('5', '2')], 21)
        self.assertEqual(distances[('5', '3')], 11)
        self.assertEqual(distances[('5', '4')], 6)
        self.assertEqual(distances[('5', '6')], 9)
        
        self.assertEqual(distances[('6', '1')], 11)
        self.assertEqual(distances[('6', '2')], 12)
        self.assertEqual(distances[('6', '3')], 2)
        self.assertEqual(distances[('6', '4')], 13)
        self.assertEqual(distances[('6', '5')], 9)
        