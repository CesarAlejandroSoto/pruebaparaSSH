from numpy import * #importa la libreria numpy
from matplotlib.pyplot import *
import math

agua= array([10,20,30,40,50,60,70,80,90,100])
produccion = array([100,200,400,600,800,1000,1100,1200,1250,1300])

scatter(agua,produccion)
xlabel("cantidad de agua aplicada")
ylabel("produccion de los cultivos")
show()

if produccion.max() == produccion[-1]:
    print('No se puede determinar la cantidad optima de agua')
else:
    cantidad_optima = agua[argmax(produccion)];
    print('La cantidad optima a aplicar de agua es de', cantidad_optima,'litros')

