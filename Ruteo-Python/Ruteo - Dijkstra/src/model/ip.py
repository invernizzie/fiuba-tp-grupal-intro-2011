from string import atoi

class Ip(object):
    
    def __init__(self, str_ip):
        ip_str, mask_str = str_ip.split('/')
        
        self.mask = get_mask_from_str(mask_str)
        self.ip = get_ip_from_str(ip_str)
        
    def get_net_ip_number(self):
        return self.ip & self.mask
        
    def get_net_ip(self):
        net_ip = self.get_net_ip_number()
        net_str = get_str_from_ip(net_ip)
        mask_str = get_str_from_mask(self.mask)
        ip_str = net_str + '/' + mask_str
        return Ip(ip_str)
    
    def is_in_net(self, ip):
        return self.get_net_ip_number() == (ip.ip & self.mask)

    def get_ip_str(self):
        return get_str_from_ip(self.ip)
    
    def get_ip_mask_str(self):
        return get_str_from_ip(self.mask)
    
    def __str__(self):
        str_ip = get_str_from_ip(self.ip)
        str_mask = get_str_from_mask(self.mask)
        return str_ip + '/' + str_mask
        
    def __eq__(self, other):
        return self.__str__() == other.__str__()
    
    def __hash__(self):
        return hash(self.__str__())
            
def get_ip_from_str(ip_str):
    ip_bytes = ip_str.split('.')
    
    byte_0 = atoi(ip_bytes[3])
    byte_1 = atoi(ip_bytes[2]) << 8
    byte_2 = atoi(ip_bytes[1]) << 16
    byte_3 = atoi(ip_bytes[0]) << 24
             
    return byte_0 + byte_1 + byte_2 + byte_3

def get_str_from_ip(ip):
    
    byte_0 = ip & 0x000000FF
    byte_1 = (ip & 0x0000FF00) >> 8
    byte_2 = (ip & 0x00FF0000) >> 16
    byte_3 = (ip & 0xFF000000) >> 24
    
    return str(byte_3) + '.' + str(byte_2) + '.' + str(byte_1) + '.' + str(byte_0)

def get_mask_from_str(mask_nro_bits_str):
    nro_bits = atoi(mask_nro_bits_str)
    mask = 0xFFFFFFFF
    return (mask << (32 - nro_bits)) & mask       

def get_str_from_mask(mask):
    zeros_count = 0
    aux_mask = mask
    while ((aux_mask % 2) == 0):
        aux_mask = aux_mask / 2
        zeros_count += 1
    
    bit_count = 32 - zeros_count
    check_mask = get_mask_from_str(str(bit_count))
    if (mask != check_mask):
        raise "Wrong mask"
    
    return str(bit_count)