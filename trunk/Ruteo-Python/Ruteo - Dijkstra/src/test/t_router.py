import unittest
from model.ip import Ip
from model.router import Router

class TestRouter(unittest.TestCase):
    
    def setUp(self):
        interfaces_1 = [Ip('10.10.0.8/8'),\
                        Ip('172.40.0.87/16'),\
                        Ip('192.168.0.1/24'),\
                        Ip('192.168.0.65/27') ]
        
        interfaces_2 = [Ip('10.10.0.9/8'),\
                        Ip('172.40.0.88/16'),\
                        Ip('192.168.0.2/24'),\
                        Ip('192.168.0.03/27') ]
        
        self.router_1 = Router(interfaces_1, 'r1')
        self.router_2 = Router(interfaces_2, 'r2')
            
    def tearDown(self):
        self.router_1 = None
        self.router_2 = None
        
    def test_get_connected_networks(self):
        networks = self.router_1.get_connected_networks()
        
        self.assertEqual(networks[0].get_net_ip(), '10.0.0.0/8')
        self.assertEqual(networks[1].get_net_ip(), '172.40.0.0/16')
        self.assertEqual(networks[2].get_net_ip(), '192.168.0.0/24')
        self.assertEqual(networks[3].get_net_ip(), '192.168.0.64/27')
        
    def test_is_connected_to_net(self):
        self.assertTrue(self.router_1.is_connected_to_net(Ip('10.0.0.0/8')))
        self.assertTrue(self.router_1.is_connected_to_net(Ip('172.40.0.0/16')))
        self.assertTrue(self.router_1.is_connected_to_net(Ip('192.168.0.0/24')))
        self.assertTrue(self.router_1.is_connected_to_net(Ip('192.168.0.64/27')))
      
    def test_get_link_interfaces(self):
        links = self.router_1.get_link_interfaces(self.router_2)
        
        self.assertEqual(links[0], Ip('10.10.0.8/8'))
        self.assertEqual(links[1], Ip('10.10.0.9/8'))