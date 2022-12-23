class program:
    def __init__(self,H_dist,Graph_nodes):
        self.H_dist=H_dist
        self.Graph_nodes=Graph_nodes

    def aStarAlgo(self,start_node, stop_node):
        open_set = set(start_node)
        closed_set = set()
        g = {} 
        parents = {}
        g[start_node] = 0
        parents[start_node] = start_node
        while len(open_set) > 0 :
            n = None
            for v in open_set:
                if n == None or g[v] + self.heuristic(v) < g[n] + self.heuristic(n):
                    n = v
            if n == stop_node or self.Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in self.get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)   
                        parents[m] = n     
                        g[m] = g[n] + weight 
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                print('Path found: {}'.format(path))
                return path
            open_set.remove(n)
            closed_set.add(n) 
        print('Path does not exist!')
        return None

    def get_neighbors(self,v):
        if v in self.Graph_nodes:
            return self.Graph_nodes[v]
        else:
            return None
    

    def heuristic(self,n):
        return self.H_dist[n]