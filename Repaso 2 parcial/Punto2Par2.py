from itertools import *

'''1. ¿De cuantas maneras ordenadas puede programar un director de televisión seis comerciales en los seis 
intermedios para comerciales durante la transmisión televisiva del primer tiempo de un partido de Futbol?,
si: 
a) los comerciales son todos diferentes. 
b) dos de los comerciales son iguales. 
c) Si hay cuatro comerciales diferentes, uno de los cuales debe aparecer tres veces, mientras que cada uno 
de los otros debe aparecer una sola vez.
'''

class Intermedios:
    def comercialesDiferentes (self):
        self.listaComerDiferentes = [1,2,3,4,5,6];
        self.permutacion1 = permutations(self.listaComerDiferentes);
        self.contador1 =0;
        for elememto in list(self.permutacion1):
            self.lista1 = list(elememto);
            self.contador1 = self.contador1+1;
            print(elememto);
        print("Las maneras para que el director pueda transmitir comerciales diferentes en los intermedios son:",self.contador1);
    def dosComercialesIguales (self):
        self.listadosComercialesIg = [1,2,3,4];
        self.permutacion2 = permutations(self.listadosComercialesIg);
        self.contador2 =0;
        for elemento in list(self.permutacion2):
            self.lista2 = list(elemento);
            self.lista2.insert(0,5);
            self.lista2.insert(0,6);
            self.contador2 = self.contador2 + 1;
            print(elemento);
        print("Las maneras para que el director de TV pueda transmitir dos comerciales iguales son:",self.contador2);
    def cuatroComercialesDif (self):
        self.listaCuatroComerDif = [1,2,3];
        self.permutacion3 = permutations(self.listaCuatroComerDif,3);
        self.contador3 = 0;
        for elemento in list(self.permutacion3):
            self.lista3 = list(elemento);
            self.lista3.insert(0,4);
            self.lista3.insert(0,4);
            self.lista3.insert(0,4);
            self.contador3 = self.contador3 + 1;
            print(elemento);
        
        self.listaCuatroComerDif = [1,2,3];
        self.permutacion4 = permutations(self.listaCuatroComerDif,1);
        self.contador4 = 0;
        for elemento in list(self.permutacion4):
            self.lista3 = list(elemento);
            self.lista3.insert(0,4);
            self.lista3.insert(0,4);
            self.lista3.insert(0,4);
            self.contador4 = self.contador4 + 1;
            print(elemento);
        
        self.listaCuatroComerDif = [1,2,3];
        self.permutacion5 = permutations(self.listaCuatroComerDif,1);
        self.contador5 = 0;
        for elemento in list(self.permutacion5):
            self.lista3 = list(elemento);
            self.lista3.insert(0,4);
            self.lista3.insert(0,4);
            self.lista3.insert(0,4);
            self.contador5 = self.contador5 + 1;
            print(elemento);
        
        print("Las maneras para que el director de TV pueda transmitir cuatro comerciales diferentes y que uno se repita 3 veces son: ",4*self.contador3*self.contador4*self.contador5);
        
Director= Intermedios();
Director.comercialesDiferentes();
Director.dosComercialesIguales();
Director.cuatroComercialesDif();
