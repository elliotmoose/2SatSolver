import basic.cnfgraph as graph
import basic.parser as parser
def test():
    """
    automated test to test functionality of functions
    """
    print("=====Running Tests=====\n")
    print("negate(): ", "PASS" if graph.negate("-1") == "1" and graph.negate("1") == "-1" else "FAIL")
    
    clauses = parser.parse_cnf_file_to_clauses(parser.INPUT_FILE_PATH) 

    # edges = graph.edges_from_clauses([["1","2"]])
    edges = graph.edges_from_clauses(clauses)
    print("\nedges_from_clauses():", "PASS" if edges == [["-1","2"],["-2","1"]] else "FAIL")
    print("")
    nodes =  graph.graph_nodes_from_edges(edges)
    # print(edges)
    print(", \n".join(str(node) for node in nodes.values()))
    print("\ngraph_nodes_from_edges():", "PASS" if graph.graph_nodes_from_edges([["1","2"]]) == [["-1","2"],["-2","1"]] else "FAIL")
    

test()