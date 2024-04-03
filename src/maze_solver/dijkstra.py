import numpy as np
import random
from .utils import maze_to_graph, print_dict
from .depth_first import DF_search



class BF_search:

    def __init__(self):

        self.graph = None
        self.order = []
        self.queue = []

    def init_graph(self, maze, start):

        self.__init__()

        DF = DF_search()
        DF.init_graph(maze)
        sep_trees = DF.separate_trees()

        for tree in sep_trees:
            if start in tree.keys():
                self.graph = tree

        for node in self.graph:

            self.graph[node] = { "adj": self.graph[node]["adj"],
                                 "dist": 10000,
                                 "prev": None }
            
            self.queue.append(node)

    def search_maze(self, start, target):

        self.order = [start]
        self.graph[start]["dist"] = 0

        while len(self.queue) > 0:

            # get node with minimum distance that is in q
            min = None
            for node in self.queue:
                if min == None:
                    min = self.graph[node]["dist"]
                    min_node = node
                elif self.graph[node]["dist"] < min:
                    min = self.graph[node]["dist"]
                    min_node = node

            self.queue.remove(min_node)  # remove said node from queue

            for adj in self.graph[min_node]["adj"]:
                if adj in self.queue:
                    self.order.append(adj)
                    self.update_distance(min_node, adj)
                    if target != None and adj == target:
                        return

    def update_distance(self, min_node, adj):
        alt = self.graph[min_node]["dist"] + 1
        if alt < self.graph[adj]["dist"]:
                self.graph[adj]["dist"] = alt
                self.graph[adj]["prev"] = min_node 

    def gen_path(self, target):
        
        if target not in self.graph.keys():
            return []
        
        path = [target]
        node = target

        while self.graph[node]["prev"] != None:
            node = self.graph[node]["prev"]
            path.insert(0, node)

        return path

if __name__ == "__main__":

    maze = np.array([
                    [1,1,1,1,1],
                    [1,0,1,1,1],
                    [1,0,0,0,1],
                    [1,1,0,0,1],
                    [1,1,1,1,1]
                    ])

    BF = BF_search()
    BF.init_graph(maze, (1,1))
    BF.search_maze((1,1), (3,3))
    print(BF.gen_path((3,3)))


