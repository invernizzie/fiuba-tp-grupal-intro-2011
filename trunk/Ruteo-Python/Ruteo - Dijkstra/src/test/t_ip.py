import unittest
from model.ip import Ip, get_str_from_ip, get_ip_from_str, get_mask_from_str,\
    get_str_from_mask

class TestIp(unittest.TestCase):
    
    def setUp(self):
        self.ip_a = Ip('10.10.0.8/8')
        self.ip_b = Ip('172.40.0.87/16')
        self.ip_c = Ip('192.168.0.1/24')
        self.ip_sub = Ip('192.168.0.65/27')
            
    def tearDown(self):
        self.ip_a = None
        self.ip_b = None
        self.ip_c = None
        self.ip_sub = None
    
    def test_net_ip(self):
        net_a = self.ip_a.get_net_ip_number()
        net_b = self.ip_b.get_net_ip_number()
        net_c = self.ip_c.get_net_ip_number()
        net_sub = self.ip_sub.get_net_ip_number()
        
        self.assertEqual(get_str_from_ip(net_a), '10.0.0.0')
        self.assertEqual(get_str_from_ip(net_b), '172.40.0.0')
        self.assertEqual(get_str_from_ip(net_c), '192.168.0.0')
        self.assertEqual(get_str_from_ip(net_sub), '192.168.0.64')
    
    def test_is_in_net(self):
    
        ip_a = Ip('10.255.255.255/8')
        ip_b = Ip('172.40.255.255/16')
        ip_c = Ip('192.168.0.255/24')
        ip_sub = Ip('192.168.0.95/27')
    
        self.assertTrue(self.ip_a.is_in_net(ip_a))
        self.assertTrue(self.ip_b.is_in_net(ip_b))
        self.assertTrue(self.ip_c.is_in_net(ip_c))
        self.assertTrue(self.ip_sub.is_in_net(ip_sub))        
    
    def test_is_not_in_net(self):
        pass
    
    def test_ip_from_str(self):
        ip1 = get_ip_from_str('0.0.0.1')
        ip2 = get_ip_from_str('0.0.1.0')
        ip3 = get_ip_from_str('0.1.0.0')
        ip4 = get_ip_from_str('1.0.0.0')
         
        ip5 = get_ip_from_str('255.255.255.255') 
        ip6 = get_ip_from_str('0.0.0.0') 
        
        self.assertEqual(ip1, 256 ** 0)
        self.assertEqual(ip2, 256 ** 1)
        self.assertEqual(ip3, 256 ** 2)
        self.assertEqual(ip4, 256 ** 3)    
        
        self.assertEqual(ip5, 2 ** 32 - 1)
        self.assertEqual(ip6, 0)    
    
    def test_get_str_from_ip(self):
        ip1 = get_str_from_ip(256 ** 0)
        ip2 = get_str_from_ip(256 ** 1)
        ip3 = get_str_from_ip(256 ** 2)
        ip4 = get_str_from_ip(256 ** 3) 
        ip5 = get_str_from_ip(2 ** 32 - 1) 
        ip6 = get_str_from_ip(0) 
        
        self.assertEqual(ip1, '0.0.0.1')
        self.assertEqual(ip2, '0.0.1.0')
        self.assertEqual(ip3, '0.1.0.0')
        self.assertEqual(ip4, '1.0.0.0')    
        
        self.assertEqual(ip5, '255.255.255.255')
        self.assertEqual(ip6, '0.0.0.0')    
        
    def test_get_mask_from_str(self):
        mask1 = get_mask_from_str('8')
        mask2 = get_mask_from_str('16')
        mask3 = get_mask_from_str('24')
        mask4 = get_mask_from_str('30')
    
        self.assertEqual(mask1, get_mask(8))
        self.assertEqual(mask2, get_mask(16))
        self.assertEqual(mask3, get_mask(24))
        self.assertEqual(mask4, get_mask(30))    
        
    def test_get_str_from_mask(self):
        mask1 = get_str_from_mask(get_mask(8))
        mask2 = get_str_from_mask(get_mask(16))
        mask3 = get_str_from_mask(get_mask(24))
        mask4 = get_str_from_mask(get_mask(30))
    
        self.assertEqual(mask1, '8')
        self.assertEqual(mask2, '16')
        self.assertEqual(mask3, '24')
        self.assertEqual(mask4, '30')    
         
    def test_get_ip_str(self):
        ip_str_a = self.ip_a.get_ip_str()
        ip_str_b = self.ip_b.get_ip_str()
        ip_str_c = self.ip_c.get_ip_str()
        ip_str_ip_sub  = self.ip_sub .get_ip_str()
        
        self.assertEqual(ip_str_a, '10.10.0.8')
        self.assertEqual(ip_str_b, '172.40.0.87')
        self.assertEqual(ip_str_c, '192.168.0.1')
        self.assertEqual(ip_str_ip_sub, '192.168.0.65')
    
    def test_get_ip_mask_str(self):
        ip_str_a = self.ip_a.get_ip_mask_str()
        ip_str_b = self.ip_b.get_ip_mask_str()
        ip_str_c = self.ip_c.get_ip_mask_str()
        ip_str_ip_sub  = self.ip_sub .get_ip_mask_str()
        
        self.assertEqual(ip_str_a, '255.0.0.0')
        self.assertEqual(ip_str_b, '255.255.0.0')
        self.assertEqual(ip_str_c, '255.255.255.0')
        self.assertEqual(ip_str_ip_sub, '255.255.255.224')
            
def get_mask(num_bits):
    start = 32 - num_bits 
    result = 0
    for i in range(start, 32):
        result += 2 ** i
    return result