class Node:
    
    def __init__(self, name=0):
        self.color = None
        self.pi = None
        self.d = None
        self.f = None
        self.name = name
        #in the list we have elements
        #like this : [destination_node_name ,weight]
        self.adj = []
