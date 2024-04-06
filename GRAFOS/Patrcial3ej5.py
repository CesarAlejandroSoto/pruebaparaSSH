'''Aplicar búsquedas de algoritmos por BFS, DFS, Dijkstra
Para los siguientes grafos, se debe preguntar cual seria el nodo de inicio y cual
seria el nodo de llegada
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["Riohacha","Mingueo","S.Marta","Barranquilla","Cartagena","Arjona","C.Biso","Calamar","Fundacion","Bosconia","Valledupar","Fonseca","Albania","Plato","C. de Bolivar","Ovejas","Sincelejo","Momil","Lorica","Tolu","S.Onofre","T.Viejo","M. la baja"])
G.add_edge("Riohacha","Mingueo", weight = 70.81);
G.add_edge("Riohacha","Albania", weight = 73.6);
G.add_edge("Mingueo","S.Marta", weight = 97.7);
G.add_edge("S.Marta","Barranquilla", weight = 105);
G.add_edge("Fundacion","S.Marta", weight = 97.2);
G.add_edge("Fundacion","Calamar", weight = 218);
G.add_edge("Fundacion","Bosconia", weight = 70.9);
G.add_edge("Bosconia","Valledupar", weight = 95.8);
G.add_edge("Valledupar","Fonseca", weight = 62.2);
G.add_edge("Fonseca","Albania", weight = 52.8);
G.add_edge("Bosconia","Plato", weight = 112);
G.add_edge("Plato","C. de Bolivar", weight = 43.8);
G.add_edge("Calamar","Plato", weight = 115);
G.add_edge("Calamar","C.Biso", weight = 54.2);
G.add_edge("Calamar","Barranquilla", weight = 93.7);
G.add_edge("Barranquilla","Cartagena", weight = 119);
G.add_edge("Cartagena", "Arjona", weight = 22.8);
G.add_edge("Arjona","C.Biso", weight = 20.1);
G.add_edge("C.Biso","M. la baja", weight = 23.5);
G.add_edge("M. la baja","S.Onofre", weight = 42.8);
G.add_edge("S.Onofre","T.Viejo", weight = 38.4);
G.add_edge("T.Viejo","Tolu", weight = 19.6);
G.add_edge("T.Viejo","Sincelejo", weight = 21.7);
G.add_edge("T.Viejo","Momil", weight = 42.3);
G.add_edge("Tolu","Lorica", weight = 50.9);
G.add_edge("Lorica","Momil", weight = 16.8);
G.add_edge("Momil","Sincelejo", weight = 45);
G.add_edge("Sincelejo","Ovejas", weight = 43.5);
G.add_edge("Ovejas","C. de Bolivar", weight = 25.2);
pos = nx.spring_layout(G)
nx.draw(G,pos, with_labels = True, font_weight = "bold", node_color = "cyan", edge_color = "black")
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels = edge_weight)

path = nx.dijkstra_path(G, source = "Lorica", target = "Riohacha")
print("Ruta = ".format("Lorica", "Riohacha"),path)
distance = nx.dijkstra_path_length(G, source = "Lorica", target = "Riohacha")
print("La distancia entre = ".format("Lorica","Riohacha"), distance)
plt.show()
