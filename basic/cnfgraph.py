import node

def graph_nodes_from_edges(edges):
    #edges are defined as such: 
    #[1,2] imples a directed edge from 1 => 2        
    #NOTE: 1 and -1 are two different node.

    nodes = {}
    for edge in edges:  

        
        if nodes.get(edge[1]) == None:
            #Create new node
            forwardNode = node.Node(edge[1])
            nodes[edge[1]] = forwardNode
        else:
            #Retrieve node
            forwardNode = nodes[edge[1]]

        if nodes.get(edge[0]) == None:
            #Create new node and add connection
            thisNode = node.Node(edge[0])
            thisNode.addForwardConnection(forwardNode)
            nodes[edge[0]] = thisNode
        else:
            #Add connection
            nodes[edge[0]].addForwardConnection(forwardNode)

    return nodes


def negate(literal):
    """
    turns -1 into 1
    turns 1 into -1    
    """

    if literal[0] == "-":
        return literal[1:]
    else:
        return "-" + literal 

def edges_from_clauses(clauses):
    """
    This function takes in an array of 2 sat clauses as such
    [
        [1, 2], //A OR B
        [2, 3] //B OR C
    ]

    and turns it into implication edges as such
    [
        [-1, 2], // !A => B
        [-2, 1], // !B => A
        [-2, 3], // !B => C
        [-3, 2] // !C => B
    ]

    """
    
    edges = []

    for clause in clauses:
        literal_one = clause[0]
        literal_two = clause[1]
        edge_one = [negate(literal_one), literal_two]
        edge_two = [negate(literal_two), literal_one]

        edges.append(edge_one)
        edges.append(edge_two)

    return edges
            
            
