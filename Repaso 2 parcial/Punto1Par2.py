from itertools import *

'''2. Entre los materias que se dictan para la maestría en gestión de proyectos, que se ofrecen durante 
cierto semestre en una universidad, se dictan seis materias de contabilidad, cuatro de mercadotecnia y
tres de informática. ¿En cuántas formas se puede inscribir un estudiante en dos materias de contabilidad, 
dos de mercadotecnia y uno de informática?'''
class GestionDeProyectos:
    
    def contabilidad (self):
        self.listaContabilidad = ["ContMateria 1","ContMateria 2","ContMateria 3","ContMateria 4","ContMateria 5","ContMateria 6"];
        self.combinacionContabilidad = combinations(self.listaContabilidad,2);
        self.contador1 = 0;
        for elemento in list(self.combinacionContabilidad):
            self.lista1 = list(elemento);
            self.contador1 = self.contador1 + 1;
            print(elemento);

    def mercadotecnia (self):
        self.listaMercadotecnia = ["MercMateria 1","MercMateria 2","MercMateria 3","MercMateria 4"];
        self.combinacionMercadotecnia = combinations(self.listaMercadotecnia,2);
        self.contador2 =0;
        for elemento in list(self.combinacionMercadotecnia):
            self.lista2 = list(elemento);
            self.contador2 = self.contador2 + 1;
            print(elemento);
        
    def informatica (self):
        self.listaInformatica = ["InfMateria 1","InfMateria 2","InfMateria 3"];
        self.combinacionesInformatica = combinations(self.listaInformatica,1);
        self.contador3 = 0;
        for elemento in list(self.combinacionesInformatica):
            self.lista3 = list(elemento);
            self.contador3 = self.contador3 +1;
            print(elemento);
    
    def inscripcion (self):
        self.formas = self.contador1 * self.contador2  * self.contador3;
        print ("El numero de formas posibles que puede un estudiante inscribir 2 materias de contabilidad,\n 2 materias de mercadotecnia y una de informatica son: ", self.formas,"Formas");
estudiante = GestionDeProyectos();
estudiante.contabilidad();
estudiante.mercadotecnia();
estudiante.informatica();
estudiante.inscripcion();


