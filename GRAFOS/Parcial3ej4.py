'''Aplicar búsquedas de algoritmos por BFS, DFS, Dijkstra
Para los siguientes grafos, se debe preguntar cual seria el nodo de inicio y cual
seria el nodo de llegada
'''

import networkx as nx
import matplotlib.pyplot as plt

F = nx.Graph()
F.add_nodes_from(["A","B","C","D","E","F","G","Z"])
F.add_edge("A","B", weight = 2)
F.add_edge("A","F", weight = 1)
F.add_edge("B","D", weight = 2)
F.add_edge("D","F", weight = 3)
F.add_edge("D","E", weight = 4)
F.add_edge("B","E", weight = 4)
F.add_edge("B","C", weight = 2)
F.add_edge("C","E", weight = 3)
F.add_edge("C","Z", weight = 1)
F.add_edge("Z","G", weight = 6)
F.add_edge("E","G", weight = 7)
F.add_edge("G","F", weight = 5)

pos = nx.spring_layout(F)
nx.draw(F, pos, with_labels = True, font_weight = "bold", node_color = "cyan", edge_color= "black")
edge_weight = nx.get_edge_attributes(F, 'weight')
nx.draw_networkx_edge_labels(F,pos, edge_labels= edge_weight)

print("Por favor indique la ruta en MAYUSCULAS")
start = str(input("ingrese desde donde empezará?  "))
finish = str(input("Ingrese hasta donde llegará?  "))

path = nx.dijkstra_path(F, source = start, target = finish)
print("Ruta = ".format("desde: ", start, "hasta: ", finish), path)
distance = nx.dijkstra_path_length(F, source = start, target = finish)
print("La distancia mas corta es = ".format(start,finish),distance)
plt.show()
