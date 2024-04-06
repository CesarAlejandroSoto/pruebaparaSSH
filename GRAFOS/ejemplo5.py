import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        
    def agregar_vertice(self, vertice):
        self.grafo.add_node(vertice)
        
    def agregar_arista(self, vertice1, vertice2, weight):
        self.grafo.add_edge(vertice1, vertice2, weight=weight)
        
    def dibujar_grafo(self):
        nx.draw(self.grafo, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()
        
    def ruta_cortabfs(self, source):
        bfs_edges = nx.bfs_edges(self.grafo, source=source)
        print(list(bfs_edges))
        
    def recorridodfs(self, source):
        dfs_edges = nx.dfs_edges(self.grafo, source=source)
        print(list(dfs_edges))
        


grafo = Grafo()

# Agrega tus vértices y aristas aquí

grafo.agregar_vertice('Rioacha')
grafo.agregar_vertice('Mingueo')
grafo.agregar_vertice('S.Marta')
grafo.agregar_vertice('Barranquilla')
grafo.agregar_vertice('Cartagena')
grafo.agregar_vertice('Arjona')
grafo.agregar_vertice('C.Biso')
grafo.agregar_vertice('Calamar')
grafo.agregar_vertice('Fundacion')
grafo.agregar_vertice('Bosconia')
grafo.agregar_vertice('Valledupar')
grafo.agregar_vertice('Fonseca')
grafo.agregar_vertice('Albania')
grafo.agregar_vertice('Plato')
grafo.agregar_vertice('C. de Bolivar')
grafo.agregar_vertice('Ovejas')
grafo.agregar_vertice('Sincelejo')
grafo.agregar_vertice('Momil')
grafo.agregar_vertice('Lorica')
grafo.agregar_vertice('Tolu')
grafo.agregar_vertice('S.Onofre')
grafo.agregar_vertice('T.Viejo')
grafo.agregar_vertice('M. la baja')

grafo.agregar_arista('Rioacha', 'Mingueo', weight=70.81)
grafo.agregar_arista('Rioacha', 'Albania', weight=73.6)
grafo.agregar_arista('Mingueo', 'S.Marta', weight=97.7)
grafo.agregar_arista('S.Marta', 'Fundacion', weight=97.2)
grafo.agregar_arista('S.Marta', 'Barranquilla', weight=105)
grafo.agregar_arista('Barranquilla', 'Calamar', weight=93.7)
grafo.agregar_arista('Barranquilla', 'Cartagena', weight=119)
grafo.agregar_arista('Cartagena', 'Arjona', weight=22.8)
grafo.agregar_arista('Arjona', 'C.Biso', weight=20.1)
grafo.agregar_arista('C.Biso', 'M. la baja', weight=23.5)
grafo.agregar_arista('C.Biso', 'Calamar', weight=54.2)
grafo.agregar_arista('C.Biso', 'C. de Bolivar', weight=74.1)
grafo.agregar_arista('Calamar', 'Plato', weight=115)
grafo.agregar_arista('Calamar', 'Fundacion', weight=218)
grafo.agregar_arista('Fundacion', 'Bosconia', weight=70.9)
grafo.agregar_arista('Bosconia', 'Valledupar', weight=95.8)
grafo.agregar_arista('Bosconia', 'Plato', weight=112)
grafo.agregar_arista('Plato', 'C. de Bolivar', weight=43.8)
grafo.agregar_arista('C. de Bolivar', 'Ovejas', weight=25.2)
grafo.agregar_arista('Ovejas', 'Sincelejo', weight=43.5)
grafo.agregar_arista('Sincelejo', 'Momil', weight=45)
grafo.agregar_arista('Sincelejo', 'T.Viejo', weight=21.7)
grafo.agregar_arista('Momil', 'Lorica', weight=16.8)
grafo.agregar_arista('Momil', 'T.Viejo', weight=42.3)
grafo.agregar_arista('Lorica', 'Tolu', weight=50.9)
grafo.agregar_arista('Tolu', 'T.Viejo', weight=19.6)
grafo.agregar_arista('S.Onofre', 'T.Viejo', weight=38.4)
grafo.agregar_arista('S.Onofre', 'M. la baja', weight=42.8)
grafo.agregar_arista('Fonseca', 'Valledupar', weight=62.2)
grafo.agregar_arista('Fonseca', 'Albania', weight=52.8)

grafo.dibujar_grafo()

print("Ruta más corta con Bfs")
grafo.ruta_cortabfs('Rioacha')

print("Recorrido con Dfs")
grafo.recorridodfs('Rioacha')


