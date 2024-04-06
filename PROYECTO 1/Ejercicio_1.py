from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

tiempo=random.normal(60,2,100);
print(tiempo);
hist(tiempo,bins=10);
title("Tiempo que dura en la fila")
show();

media=mean(tiempo);
print("la media de las edades es:",media);

estandar=std(tiempo);
print("la desviacionn estandar de las edades es:",estandar);

