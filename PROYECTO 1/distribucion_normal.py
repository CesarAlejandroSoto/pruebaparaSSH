from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

edades=random.normal(40,10,1000);
print(edades);
hist(edades,bins=20);
show();

media=mean(edades);
print("la media de las edades es:",media);

estandar=std(edades);
print("la desviacionn estandar de las edades es:",estandar);

