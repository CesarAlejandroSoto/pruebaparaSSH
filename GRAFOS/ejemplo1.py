import matplotlib.pyplot  as plt
import networkx as nx

class Nodo:
    def __init__(self, valor):
        self.valor = valor;
        self.vecinos = [];
    
    def AgregarVecino(self, nodo):
        self.vecinos.append(nodo);
        
class Grafo:
    def __init__(self):
        self.nodos = [];
    
    def AgregarNodo(self,nodo):
        self.nodos.append(nodo);
    
    def ImprimirGrafo(self):
        for nodo in self.nodos:
            vecinos = ", ".join([str(vecino.valor) for vecino in nodo.vecinos]);
            print(f"Nodo {nodo.valor}: Vecinos [{vecinos}]");
        

nodo1 = Nodo("Rioacha");
nodo2 = Nodo("Mingueo");
nodo3 = Nodo("S.Marta");
nodo4 = Nodo("Barranquilla");
nodo5 = Nodo("Cartagena");
nodo6 = Nodo("Arjona");
nodo7 = Nodo("C.Biso");
nodo8 = Nodo("Calamar");
nodo9 = Nodo("Fundacion");
nodo10 = Nodo("Bosconia");
nodo11 = Nodo("Valledupar");
nodo12 = Nodo("Fonseca");
nodo13 = Nodo("Albania");
nodo14 = Nodo("Plato");
nodo15 = Nodo("C. de Bolivar");
nodo16 = Nodo("Ovejas");
nodo17 = Nodo("Sincelejo");
nodo18 = Nodo("Momil");
nodo19 = Nodo("Lorica");
nodo20 = Nodo("Tolu");
nodo21 = Nodo("S.Onofre");
nodo22 = Nodo("T.Viejo");
nodo23 = Nodo("M. la baja");


'''"Riohacha","Mingueo","S.Marta","Barranquilla","Cartagena","Arjona","C.Biso",
"Calamar","Fundacion","Bosconia","Valledupar","Fonseca","Albania","Plato","C. de Bolivar",
"Ovejas","Sincelejo","Momil","Lorica","Tolu","S.Onofre","T.Viejo","M. la baja"])'''

grafo = Grafo()

grafo.AgregarNodo(nodo1);
grafo.AgregarNodo(nodo2);
grafo.AgregarNodo(nodo3);
grafo.AgregarNodo(nodo4);
grafo.AgregarNodo(nodo5);
grafo.AgregarNodo(nodo6);
grafo.AgregarNodo(nodo7);
grafo.AgregarNodo(nodo8);
grafo.AgregarNodo(nodo9);
grafo.AgregarNodo(nodo10);
grafo.AgregarNodo(nodo11);
grafo.AgregarNodo(nodo12);
grafo.AgregarNodo(nodo13);
grafo.AgregarNodo(nodo14);
grafo.AgregarNodo(nodo15);
grafo.AgregarNodo(nodo16);
grafo.AgregarNodo(nodo17);
grafo.AgregarNodo(nodo18);
grafo.AgregarNodo(nodo19);
grafo.AgregarNodo(nodo20);
grafo.AgregarNodo(nodo21);
grafo.AgregarNodo(nodo22);
grafo.AgregarNodo(nodo23);


nodo1.AgregarVecino(nodo2);
nodo1.AgregarVecino(nodo13);
nodo2.AgregarVecino(nodo3);
nodo3.AgregarVecino(nodo9);
nodo4.AgregarVecino(nodo8);
nodo4.AgregarVecino(nodo5);
nodo5.AgregarVecino(nodo6);
nodo6.AgregarVecino(nodo7);
nodo7.AgregarVecino(nodo23);
nodo7.AgregarVecino(nodo8);
nodo7.AgregarVecino(nodo15);
nodo8.AgregarVecino(nodo14);
nodo8.AgregarVecino(nodo9);
nodo9.AgregarVecino(nodo10);
nodo10.AgregarVecino(nodo11);
nodo10.AgregarVecino(nodo14);
nodo11.AgregarVecino(nodo12);
nodo12.AgregarVecino(nodo13);
nodo14.AgregarVecino(nodo15);
nodo15.AgregarVecino(nodo16);
nodo16.AgregarVecino(nodo14);
nodo10.AgregarVecino(nodo17);
nodo17.AgregarVecino(nodo18);
nodo17.AgregarVecino(nodo22);
nodo18.AgregarVecino(nodo19);
nodo18.AgregarVecino(nodo22);
nodo19.AgregarVecino(nodo20);
nodo20.AgregarVecino(nodo22);
nodo21.AgregarVecino(nodo22);
nodo21.AgregarVecino(nodo23);



grafo.ImprimirGrafo()