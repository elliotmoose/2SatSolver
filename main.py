import basic.cnfgraph as cnfgraph
import basic.parser as parser

clauses = parser.parse_cnf_file_to_clauses(parser.INPUT_FILE_PATH)
edges = cnfgraph.edges_from_clauses(clauses)
nodes =  cnfgraph.graph_nodes_from_edges(edges)
print(", \n".join(str(node) for node in nodes.values()))




