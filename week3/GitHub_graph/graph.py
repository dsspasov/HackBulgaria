# graph.py
class DirectedGraph:

    def __init__(self):
        self.links = []
        self.nodes = []

    def add_edge(self, nodeA, nodeB):
        if nodeA not in self.nodes:
            self.nodes.append(nodeA)
        if nodeB not in self.nodes:
            self.nodes.append(nodeB)
        if (nodeA, nodeB) not in self.links:
            self.links.append((nodeA, nodeB))

    def get_neighbours_for(self, nodeA):
        result = []
        if nodeA not in self.nodes:
            return result
        else:
            for link in self.links:
                if nodeA == link[0]:
                    result.append(link[1])
            return result

    def path_between(self, node_a, node_b):
        if (node_a, node_b) in self.links:
            return True
        n = self.get_neighbours_for(node_a)
        for node in n:
            if self.path_between(node, node_b):
                return True
        return False

    def __str__(self):
        s = ''
        for each_link in self.links:
            s += each_link[0] + '->' + each_link[1]+'\n'
        return s
