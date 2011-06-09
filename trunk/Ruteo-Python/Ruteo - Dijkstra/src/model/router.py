class Router(object):
    
    def __init__(self, interfaces, id):
        '''
            interfaces: lista de interfaces que contiene el ruter. 
            Las mismas deben pertenecer a la clase Ip. 
        '''
        
        self.interfaces = interfaces
        self.id = id
        
    def get_connected_networks(self):
        '''
            Retorna las redes (ips) a las cuales se encuentra conectado el router
            a travez de sus interfaces.
        '''
        
        nets = []
        for interface in self.interfaces:
            net_ip = interface.get_net_ip()
            nets.append(net_ip)
            
        return nets
    
    def is_connected_to_net(self, net):
        '''
            Nos informa si el router esta conectado a la red 'net'.
        '''
        
        return self.get_connected_networks().count(net) > 0
    
    def get_link_interfaces(self, router):
        '''
            Retorna las interfaces de ambos routers por las cuales se encuentran conectados.
            Si existe mas de una conexion entre ambos router retorna el primer enlace que encuentra.
        '''
        
        for self_interface in self.interfaces:
            for other_interface in router.interfaces:
                if self_interface.is_in_net(other_interface):
                    return (self_interface, other_interface)
    
    def __str__(self):
        return self.id + ' - ' + get_interfaces_str(self.interfaces)
    
def get_interfaces_str(interfaces):
    string = ''
    for interface in interfaces:
        string += str(interface)
        string += ' '
    return string        