import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        self.graph = Graph()
        
        self.node1 = 'node1'
        self.node2 = 'node2'
        
        self.graph.add_vertex(self.node1)
        self.graph.add_vertex(self.node2)
        self.graph.add_edge(self.node1, self.node2, 5)
        
        self.neighbors_node1 = self.graph.neighbors[self.node1]
        self.neighbors_node2 = self.graph.neighbors[self.node2]
        
    def tearDown(self):
        self.graph = None
        
    def test_vertex_size(self):
        vertexs = self.graph.vertexs
        size = len(vertexs)
        
        self.assertEquals(size, 2)
        
    def test_neighbors_size(self):
        size_node1 = len(self.neighbors_node1)
        size_node2 = len(self.neighbors_node2)
        
        self.assertEquals(size_node1, 1)
        self.assertEquals(size_node2, 1)
        
    def test_neighbors(self):
        self.assertTrue(self.node1 in self.neighbors_node2)
        self.assertTrue(self.node2 in self.neighbors_node1)
        
    def test_distance(self):
        distances = self.graph.distances
        
        distance12 = distances[(self.node1, self.node2)]
        distance21 = distances[(self.node2, self.node1)]
        
        self.assertEquals(distance12, 5)
        self.assertEquals(distance21, 5)
        self.assertEquals(distance12, distance21)