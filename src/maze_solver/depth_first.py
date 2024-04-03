import numpy as np
import random
from .utils import maze_to_graph, print_dict

class DF_search:

    def __init__(self):

        self.graph = None
        self.order = []

    def init_graph(self, maze):

        self.graph = maze_to_graph(maze)
        self.order = []

        for node in self.graph:

            self.graph[node] = { "adj": self.graph[node],
                                 "disc":   False,
                                 "prev":  None}
    
    def separate_trees(self):

        sep_trees = []

        while len(self.graph) != 0:
            keys = list(self.graph.keys())
            self.search_maze(keys[0])
            
            sep_tree = {key: value for key, value in self.graph.items() if key in self.order}
            self.graph = {key: value for key, value in self.graph.items() if key not in self.order}
        
            sep_trees.append(sep_tree)
            self.order = []

        return sep_trees

    def search_maze(self, node, target = None):

        self.graph[node]["disc"] = True
        self.order.append(node)

        if node == target: return True

        for adj in self.graph[node]["adj"]:
            if self.graph[adj]["disc"] == False:
                self.graph[adj]["prev"] = node
                if self.search_maze(adj, target): return True

        return False

    def gen_path(self, target):
        
        path = [target]
        node = target

        while self.graph[node]["prev"] != None:
            node = self.graph[node]["prev"]
            path.insert(0, node)

        return path



if __name__ == "__main__":

    maze = np.array([
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,1,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1]
                    ])

    DF = DF_search()
    DF.init_graph(maze)
    DF.search_maze((1,1), (3,3))
    print(DF.order)
