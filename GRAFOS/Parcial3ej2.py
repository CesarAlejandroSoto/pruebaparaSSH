'''Aplicar búsquedas de algoritmos por BFS, DFS, Dijkstra
Para los siguientes grafos, se debe preguntar cual seria el nodo de inicio y cual
seria el nodo de llegada
'''
import networkx as nx
import matplotlib.pyplot as plt

#SECOND EXERCISE
J = nx.Graph()
J.add_nodes_from(["Bogota","Lima","Quito","La Paz","Asunción","B. Aires"])
J.add_edge("Bogota","Quito", weight = 2)
J.add_edge("Bogota","Lima", weight = 4)
J.add_edge("Lima","Quito", weight = 1)
J.add_edge("Quito","La Paz", weight = 8)
J.add_edge("Quito","Asunción", weight = 10)
J.add_edge("Lima","Asunción", weight = 7)
J.add_edge("Lima","La Paz", weight = 5)
J.add_edge("La Paz","Asunción", weight = 2)
J.add_edge("B. Aires","La Paz", weight = 6)
J.add_edge("B. Aires","Asunción", weight = 3)

pos = nx.spring_layout(J)
nx.draw(J, pos, with_labels = True, font_weight = "bold", node_color = "cyan", edge_color= "black")
edge_weight = nx.get_edge_attributes(J, 'weight')
nx.draw_networkx_edge_labels(J,pos, edge_labels= edge_weight)

start = str(input("ingrese desde donde empezará?  "))
finish = str(input("Ingrese hasta donde llegará?  "))

path = nx.dijkstra_path(J, source = start, target = finish)
print("Ruta = ".format("desde: ", start, "hasta: ", finish), path)
distance = nx.dijkstra_path_length(J, source = start, target = finish)
print("La distancia mas corta es = ".format(start,finish),distance)
plt.show()
