import ConfigParser
from model.ip import Ip
from model.router import Router
from graph import Graph
from dijkstra import Dijkstra

class Network(object):
    
    def __init__(self, network_file):
        net = ConfigParser.ConfigParser()
        net.read(network_file)
        
        self.routers = []
        for section in net.sections():
            ips = []
            for item in net.items(section):
                ip = Ip(item[1])
                ips.append(ip)
            router = Router(ips, section)
            self.routers.append(router)
            
        self.paths = self._get_paths_distances()
        self.nets = self._get_nets()
            
    def _get_paths_distances(self):
        network = Graph()
        for vertex in self.routers:
            network.add_vertex(vertex)
        
        # Recorremos inncesariamente dos veces!
        for r1 in self.routers:
            for r2 in self.routers:
                link = r1.get_link_interfaces(r2)
                if link != None:
                    network.add_edge(r1, r2)
        
        d = Dijkstra(network)
        return d.execute()
    
    def get_routers(self):
        return self.routers

    def _get_nets(self):
        nets = set()
        
        for r in self.routers:
            networks = set(r.get_connected_networks())
            nets = nets.union(networks)
            
        return nets
    
    def get_destination_nets_from_router(self, router):
        '''
            Obtiene las redes a las cuales debe llegar 'router'. No incluye
            las redes a las que pertenece dicho router.
        '''
        
        all_nets = self.nets.copy()
        router_connected_nets = set(router.get_connected_networks())
        
        all_nets = all_nets.difference(router_connected_nets)
        
        return all_nets

    def get_destination_nets(self):
        '''
            Obtiene un diccionario que tiene como clave un router y como valor las
            redes a las cuales debe llegar. 
            No incluye las redes a las que pertenece dicho router.
        '''
        
        router_nets = {}
        for router in self.routers:
            router_nets[router] = self.get_destination_nets_from_router(router) 

    def get_route_table(self, router):
        '''
            Obtiene la tabla de ruteo de 'router'. La misma consiste en una lista de 
            tres elementos:
                            - Ip de red
                            - Mascara de red
                            - Metric (no hace falta para por cuestion de prueba se agrega)
                            - Salida (Gateway)
        '''
        
        route_table = []
        # Obtenemos las redes a las cuales se debe conectar el router.
        nets = self.get_destination_nets_from_router(router)
        for net in nets:
            gateway, metric = self.get_gateway_to_network(router, net)
            ip_net = net.get_ip_str()
            mask_net = net.get_ip_mask_str()
            entry = (ip_net, mask_net, metric, gateway)
            route_table.append(entry)
        
        return route_table
                    
    def get_gateway_to_network(self, router, net):
        '''
            Retorna una tupla con la salida de 'router' por la cual se llega a
            'net' con distancia minima y tambien se incluye dicha distancia.
        '''
        
        # Obtenemos los routers a los cuales debe llegar para alcanzar la 'net'
        routers_in_net = self.get_routers_in_net(net)
        # Es posible que haya mas de un router en la red que debemos alcanzar,
        # por lo tanto, solo tenemos en cuanta en de camino minimo. 
        goal_router = None 
        goal_distance = 9999999
        
        for router_in_net in routers_in_net:
            if router_in_net != router:
                distance = self.get_distance_between_routers(router, router_in_net)
                if distance < goal_distance:
                    goal_router = router_in_net
                    goal_distance = distance
            
        # Obtenemos la interfaz de salida.
        path = self.paths[0][(router, goal_router)] 
        # El primer salto corresponde con el segundo elemento de la lista, ya que
        # el primer elemento es el router de partida.
        first_hop = path[1] 
        # Obtenemos el gateway. get_link_interfaces retorna las interfaces
        # de los dos routers en cuestion. El primer elemento de la tupla
        # corresponde con el link en el router 'first_hop' 
        link = first_hop.get_link_interfaces(router)[0]
        str_link = link.get_ip_str()
        return (str_link, goal_distance) 
                
    def get_distance_between_routers(self, router1, router2):
        distances = self.paths[1]
        return distances[(router1, router2)]              
        
    def get_routers_in_net(self, net):
        '''
            Obtiene los routers que tienen alguna de sus interfaces en la red 'net'.
        ''' 
        
        routers = []
        for router in self.routers:
            if router.is_connected_to_net(net):
                routers.append(router)
        
        return routers 
    
    def get_route_tables(self):
        '''
            Obtiene un diccionario que tiene como clave un router y como valor la
            tabla de ruteo de cada uno de ellos. Ver get_route_table.
        '''

        route_tables = {}
        for router in self.routers:
            route_tables[router] = self.get_route_table(router)
                
        return route_tables