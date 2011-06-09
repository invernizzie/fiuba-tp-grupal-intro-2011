import ConfigParser

def build_topology_file(path):
    '''
        Crea una topologia.
    '''
    file = open(path,'w')
    parser = ConfigParser.ConfigParser() 

    parser.add_section('router-1')
    parser.set('router-1', 'eth0', '192.168.0.1/24')
    parser.set('router-1', 'eth1', '192.168.1.1/24')
    parser.set('router-1', 'eth2', '192.168.2.1/24')
    
    parser.add_section('router-2')
    parser.set('router-2', 'eth0', '192.168.0.2/24')
    parser.set('router-2', 'eth1', '192.168.3.1/24')
    parser.set('router-2', 'eth2', '192.168.4.1/24')
    
    parser.add_section('router-3')
    parser.set('router-3', 'eth0', '192.168.1.2/24')
    parser.set('router-3', 'eth1', '192.168.3.2/24')
    parser.set('router-3', 'eth2', '192.168.5.1/24')
    parser.set('router-3', 'eth3', '192.168.8.1/24')
    
    parser.add_section('router-4')
    parser.set('router-4', 'eth0', '192.168.4.2/24')
    parser.set('router-4', 'eth1', '192.168.5.2/24')
    parser.set('router-4', 'eth2', '192.168.6.1/24')
    
    parser.add_section('router-5')
    parser.set('router-5', 'eth0', '192.168.6.2/24')
    parser.set('router-5', 'eth1', '192.168.7.1/24')
    
    parser.add_section('router-6')
    parser.set('router-6', 'eth0', '192.168.7.2/24')
    parser.set('router-6', 'eth1', '192.168.8.2/24')
    parser.set('router-6', 'eth1', '192.168.2.2/24')
        
    parser.write(file)
    
    file.close()

# Builds the topology.
build_topology_file("topology.net")