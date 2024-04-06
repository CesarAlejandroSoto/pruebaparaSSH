'''Aplicar búsquedas de algoritmos por BFS, DFS, Dijkstra
Para los siguientes grafos, se debe preguntar cual seria el nodo de inicio y cual
seria el nodo de llegada
'''

import networkx as nx
import matplotlib.pyplot as plt


#THIRD EXERCISE
S = nx.Graph()
S.add_nodes_from([0,1,2,3,4,5,6,7,8])
S.add_edge(0,1, weight = 4)
S.add_edge(0,6, weight = 7)
S.add_edge(1,6, weight = 11)
S.add_edge(1,7, weight = 20)
S.add_edge(1,2, weight = 9)
S.add_edge(6,7, weight = 1)
S.add_edge(4,2 ,weight = 2)
S.add_edge(4,7, weight = 1)
S.add_edge(4,3, weight = 10)
S.add_edge(4,8, weight = 5)
S.add_edge(4,5, weight = 15)
S.add_edge(7,8, weight = 3)
S.add_edge(2,3, weight = 6)
S.add_edge(3,5, weight = 5)
S.add_edge(8,5, weight = 12)

pos = nx.spring_layout(S)
nx.draw(S, pos, with_labels = True, font_weight = "bold", node_color = "cyan", edge_color= "black")
edge_weight = nx.get_edge_attributes(S, 'weight')
nx.draw_networkx_edge_labels(S,pos, edge_labels= edge_weight)

start = int(input("ingrese desde donde empezará?  "))
finish = int(input("Ingrese hasta donde llegará?  "))

path = nx.dijkstra_path(S, source = start, target = finish)
print("Ruta = ".format("desde: ", start, "hasta: ", finish), path)
distance = nx.dijkstra_path_length(S, source = start, target = finish)
print("La distancia mas corta es = ".format(start,finish),distance)
plt.show()
