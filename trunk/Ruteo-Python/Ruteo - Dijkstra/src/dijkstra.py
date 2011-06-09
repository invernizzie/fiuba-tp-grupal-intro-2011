class Dijkstra(object):
    '''
        Dijkstra realiza el algoritmo de caminos minimos a todos los nodos de un grafo.
    '''
    
    def __init__(self, graph):
        '''
            graph: objeto de clase Graph
            paths: diccionario que tiene como clave un nodo y como valor los caminos y las distancias minimas 
                   de ese nodo al resto de los nodos del grafo.
        '''
        
        self.graph = graph
        
    def _min_distance_node(self, nodes, visited):
        '''
            Metodo auxiliar utilizado para encontrar el nodo visitado de menor distancia.
        '''
        
        min_node = None
        
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        
        return min_node

    def _execute(self, vertex):
        '''
            Dado un vertice inicial, se calcula el camino minimo al resto de los nodos del grafo junto con las 
            distancias a ellos. 
            Retorna un diccionario que tiene como clave un nodo y como valor los caminos y las distancias minimas 
            de ese nodo al resto de los nodos del grafo.
        '''
        
        # Se podria optimizar haciendo que este diccionario contenga aquellos nodos ya calculados.
        visited = {vertex : 0}
        path = {}
    
        nodes = set(self.graph.vertexs)
        
        while nodes:
            min_node = self._min_distance_node(nodes, visited)
            
            if min_node is None:
                break
    
            nodes.remove(min_node)
            cur_wt = visited[min_node]
            
            # Iteramos sobre los nodos adyacentes.
            for neighbor in self.graph.neighbors[min_node]:
                wt = cur_wt + self.graph.distances[(min_node, neighbor)]
                # Si el nodo adyacente no fue visitado o la distancia por este nuevo camino es menor.
                if neighbor not in visited or wt < visited[neighbor]:
                    # Almacenamos la nueva distancia y el predecesor para luego poder armar el camino completo.
                    visited[neighbor] = wt
                    path[neighbor] = min_node
            
        return (visited, path)
    
    def execute(self):
        '''
            Calcula los caminos minimos de todos los nodos del grafo. 
            Retorna un diccionario que tiene como clave dos nodos y como valor una lista con aquellos
            nodos que forman el camino minimo entre ambos dos.
        '''        
        
        min_paths = {}
        distances = {}
        
        for vertex in self.graph.vertexs:
            raw_distances, paths = self._execute(vertex)
            
            # Agregamos los caminos desde vextex al resto de los nodos.
            for path in paths.iterkeys():
                
                route = [path]
                goal = path

                while path != vertex:
                    route.append(paths[path])
                    path  = paths[path]
        
                route.reverse()
                min_paths[(vertex, goal)] = route 
                distances[(vertex, goal)] = raw_distances[goal]
                
        return (min_paths, distances)