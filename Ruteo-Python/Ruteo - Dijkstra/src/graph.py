class Graph(object):
    '''
        Graph representa un grafo no dirigido.
    '''
    
    def __init__(self):
        '''
            vertexs:    conjunto de nodos del grafo.
            neighbors:  diccionario que tiene como clave a un nodo y como valor a los vecinos de ese nodo.
            distancias: diccionario que tiene como clave dos nodos y como valor la distancia entre ellos.            
        '''
        self.vertexs = set()
        self.neighbors = {}
        self.distances = {}
    
    def add_vertex(self, vertex):
        self.vertexs.add(vertex)
    
    def add_edge(self, from_node, to_node, distance = 1):
        '''
            Agrega una arista entre dos nodos con peso 'distancia'. Como el grafo no es dirigido se agrega 
            la relacion dos veces invirtiendo el orden de los nodos.
        '''
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.neighbors.setdefault(from_node, [])
        self.neighbors[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance