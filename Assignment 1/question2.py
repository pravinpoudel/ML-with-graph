
from tkinter.tix import Tree
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph();
V = {1, 2, 3, 4, 5, 6}
E = [(1, 3), (4, 1), (4,2), (4, 5), (4, 6), (6, 1), (6, 2), (6, 4)]
G.add_nodes_from(V)
G.add_edges_from(E)
print(G.in_degree())

# 1. in-degrees and out-degrees of node 2 and 6
I2 = G.in_degree(2)
I6 = G.in_degree(6)
O2 = G.out_degree(2)
O6 = G.out_degree(6)
print("\n  #1. in-degrees and out-degrees of node 2 and 6 are ", I2, ", ", I6,", ", O2,", ", O6, " respectively",  "\n")
# 2. What is the shortest path from node 4 to 3?
S = nx.shortest_path(G, 4, 3)
print("\n  #2. the shortest path from node 4 to 3 is ", S,  "\n")
# 3. Is the graph a strongly connected graph?
SC = nx.is_strongly_connected(G)
print("\n  #3. is this graph strongly connected? :", SC,  "\n")
# 4. What is the largest subgraph that is strongly connected?
largest = max(nx.strongly_connected_components(G), key=len)
print("\n #4. largest connected subgraph is", largest,  "\n")
# 5. Is the graph a directed acyclic graph?
DAG = nx.is_directed_acyclic_graph(G)
print("\n  #5. Is the graph a directed acyclic graph?: ", DAG,  "\n")
# 6. What is the diameter of this graph?
# Dm = nx.diameter(G)
print("\n #6. diameter of this graph is - ","since this is  not strongly connected directed network and diameter is infinite because we have nodes which has no path to other nodes ie. infinite diameter" ,  "\n")
# 7. What is the edge list representation of πΊπΊ(πΈπΈ, ππ)?
print( "\n #7. edge list of network is ", list(G.edges()))
# 8. What is the adjacency list of πΊπΊ(πΈπΈ, ππ)?
print( "\n #8. adjacency list of network is ", G.adj,  "\n")
# 9. What is the adjacency matrix π΄ of πΊπΊ(πΈπΈ, ππ)?
A = nx.to_numpy_matrix(G)  
print("\n #9. the adjacency matrix of graph is","\n", A,  "\n")

# 11. What is the relationship between matrices π΄ , π΅ , and πΈ ?
print("\n #11. product of out edge incidence matrix and transpose of in-edge incidence matrix gives Adjacent Matrix",  "\n")

# 12. Please draw the line graph of πΊπΊ(πΈπΈ, ππ).
plt.figure(1)
# generating the line graph from the directed graph G
H = nx.line_graph(G)
nx.draw_networkx(H, arrows = True, arrowsize=10, node_size=100, with_labels = True)
plt.show()

# 13. What is the adjacency matrix π of the line graph of πΊ(πΈ, π)?
AL = nx.to_numpy_matrix(H)
print("\n #13. the adjacency matrix of line graph is","\n", AL,  "\n")


# 14. What is the relationship the matrices M , π΅ , and πΈ?
print(" \n #14. product of transpose of in-edge incidence Matrix(E) and out-edge incidence matrix(E) is equal to M")