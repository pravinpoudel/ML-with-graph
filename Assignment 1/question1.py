from email import iterators
from turtle import pos
# import scipy as sp
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# create empty undirected graph
G = nx.Graph()

# add node
nodeList = [1, 2, 3, 4, 5, 6] # or we could have done range(6) for this case
G.add_nodes_from(nodeList);

# add edges
edgeList = [(1, 6, {"id":"c"}), (1, 3, {"id":"a"}), (1, 4, {"id":"b"}), (2, 6, {"id":"e"}), (2, 4, {"id":"d"}), (4, 5, {"id":"f"}), (4, 6, {"id":"g"})]
G.add_edges_from(edgeList)

# what are the degree of node 1 and 4
print("degree of node 1 is", len(list(G.adj[1])), "and degree of node 4 is ", len(list(G.adj[4])),  "\n")

#what is the shortest path from node 3 to node 5
shortestPath = nx.shortest_path(G, 3, 5) # compute shortest path from 3 to 5 whereas default is dijkstra
print("shortest path from node 3 to node 4 is", shortestPath, "\n")

#edge list of graph
print("edge list of the graph is", G.edges)


#adjacency list of Graph is
print("adjacency list of graph is", G.adj,  "\n")

# adjacency matrix A of graph
A = nx.to_numpy_matrix(G)  
# we could have also got it by nx.adjacency_matrix(G).toarray()
print("adjacency matrix of Graph is \n", A,  "\n");

# degree matrix 𝐷 of graph
degreeList = []
for degree1 in G.degree():
    degreeList.append(degree1[1])

D = np.diag(degreeList)
print("degree matrix of graph is \n", D,  "\n")

#laplacian matrix of graph is:
L = np.subtract(D, A)
print("Laplacian matrix of graph is \n", L,  "\n")

#Relation between A, D and C
print("difference between output matrix generated from product of incidence matrix and transpose of that incidence matrix (C*T(C)) and Degree Matrix (D) is equal to the adjacent matrix (A) of that graph \n")

#incidence matrix of Graph is:
I = nx.incidence_matrix(G).todense();
print("\n incidence matrix is ", I,  "\n")
#  draw the line graph of 𝐺𝐺(𝐸, 𝑉)
plt.figure(1)
H= nx.line_graph(G)
nx.draw_networkx(H, pos=nx.spring_layout(H, iterations = 1000),  arrows = False, with_labels = True)
plt.show()


