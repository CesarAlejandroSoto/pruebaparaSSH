import matplotlib.pyplot  as plt
import networkx as nx

nuevo_grafo = nx.Graph();
'''
nuevo_grafo.add_nodes_from(["A","B","C","D","E"]);
nuevo_grafo.add_edges_from([("A","B"),("A","C"),("B","C"),("B","D"),("C","D"),("C","E"),("D","E")]);'''

nuevo_grafo.add_node("A");
nuevo_grafo.add_node("B");
nuevo_grafo.add_node("C");
nuevo_grafo.add_node("D");
nuevo_grafo.add_node("E");
nuevo_grafo.add_node("F");
nuevo_grafo.add_node("G");
nuevo_grafo.add_node("H");
nuevo_grafo.add_node("I");
nuevo_grafo.add_node("J");
nuevo_grafo.add_node("K");


nuevo_grafo.add_edge("A","B");
nuevo_grafo.add_edge("A","C");
nuevo_grafo.add_edge("A","D");
nuevo_grafo.add_edge("B","E");
nuevo_grafo.add_edge("E","I");
nuevo_grafo.add_edge("I","F");
nuevo_grafo.add_edge("C","G");
nuevo_grafo.add_edge("G","J");
nuevo_grafo.add_edge("J","K");
nuevo_grafo.add_edge("K","H");
nuevo_grafo.add_edge("H","D");


posicion = nx.spring_layout(nuevo_grafo);

nx.draw(nuevo_grafo,posicion,with_labels = True);

plt.show();
# Mostrar recorrido BFS
print("BFS");
bfs_edges = nx.bfs_edges(nuevo_grafo,source="A");
print(list(bfs_edges));

# Mostrar recorrido DFS
print("DFS");
dfs_edges = nx.dfs_edges(nuevo_grafo,source="A");
print(list(dfs_edges));