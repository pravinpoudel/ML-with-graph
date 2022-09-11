
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

print("in-degrees and out-degrees of node 2 and 6 are ", I2, ", ", I6,", ", O2,", ", O6, " respectively")
# 2. What is the shortest path from node 4 to 3?
S = nx.shortest_path(G, 4, 3)
print("the shortest path from node 4 to 3 is ", S)
# 3. Is the graph a strongly connected graph?
SC = nx.is_strongly_connected(G)
print("is this graph strongly connected? :", SC)
# 4. What is the largest subgraph that is strongly connected?
largest = max(nx.strongly_connected_components(G), key=len)
print("largest connected subgraph is", largest)
# 5. Is the graph a directed acyclic graph?
DAG = nx.is_directed_acyclic_graph(G)
print("Is the graph a directed acyclic graph?: ", DAG)
# 6. What is the diameter of this graph?
# Dm = nx.diameter(G)
print("diameter of this graph is - ","since this is  not strongly connected directed network and diameter is infinite because we have nodes which has no path to other nodes ie. infinite diameter" )
# 7. What is the edge list representation of 𝐺𝐺(𝐸𝐸, 𝑉𝑉)?
print("edge list of network is ", list(G.edges()))
# 8. What is the adjacency list of 𝐺𝐺(𝐸𝐸, 𝑉𝑉)?
print("adjacency list of network is ", G.adj)
# 9. What is the adjacency matrix 𝐴 of 𝐺𝐺(𝐸𝐸, 𝑉𝑉)?
A = nx.to_numpy_matrix(G)  
print("the adjacency matrix of graph is", A)
# 10. What are the out-edge incidence matrix 𝐵 and the in-edge incidence matrix 𝐸 of 𝐺𝐺(𝐸, 𝑉)?
OEI = nx.incidence_matrix(G, , )
# 11. What is the relationship between matrices 𝐴 , 𝐵 , and 𝐸 ?

# 12. Please draw the line graph of 𝐺𝐺(𝐸𝐸, 𝑉𝑉).
plt.figure(1)
nx.draw_networkx(G, pos=nx.spring_layout(G, iterations = 1000),  arrows = True, arrowsize=10, node_size=100, with_labels = True)
plt.show()
# 13. What is the adjacency matrix 𝑀 of the line graph of 𝐺(𝐸, 𝑉)?
# 14. What is the relationship the matrices M , 𝐵 , and 𝐸?