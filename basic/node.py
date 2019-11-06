class Node:    
    def __init__(self, id):
        self.id = id
        self.forwardEdges = []
    
    def addForwardConnection(self, node):
        self.forwardEdges.append(node)
        

    def __str__(self):
        forwardNodeIds = []
        for node in self.forwardEdges:
            forwardNodeIds.append(node.id)
        return "Node: {0}, forwardTo: {1}".format(self.id, forwardNodeIds)