'''Dado el siguiente grafo: Realice el proceso de forma manual: 
•	Encuentre un árbol generador de peso mínimo utilizando el algoritmo de Kruskal. 

Utilizando un código del programa en Python, mediante el algoritmo de Dijkstra, encuentra la 
ruta más corta (es decir, de peso mínimo) desde el vértice A hasta el vértice G.
¿diga si es única esta ruta?
'''

import networkx as nx
import matplotlib.pyplot as plt

#FIRST EXERCISE
G = nx.Graph()
G.add_nodes_from(["A","B","C","D","E","F","G","H"])
G.add_edge("A","B", weight = 1)
G.add_edge("A","D", weight = 7)
G.add_edge("B","C", weight = 1)
G.add_edge("C","D", weight = 3)
G.add_edge("B","D", weight = 2)
G.add_edge("D","E",weight = 3)
G.add_edge("A","H", weight = 5)
G.add_edge("A","E", weight = 9)
G.add_edge("B", "E", weight = 4)
G.add_edge("E","H", weight = 1)
G.add_edge("E","G", weight = 2)
G.add_edge("E","F", weight = 6 )
G.add_edge("F","H", weight = 3)
G.add_edge("G", "H", weight = 2)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True, font_weight = "bold", node_color = "cyan", edge_color= "black")
edge_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,pos, edge_labels= edge_weight)

path = nx.dijkstra_path(G, source = "A", target = "G")
print("Ruta = ".format("desde: ", "A", "hasta: ", "G"), path)
distance = nx.dijkstra_path_length(G, source = "A", target = "G")
print("La distancia es = ".format("A","G"),distance)
plt.show()
