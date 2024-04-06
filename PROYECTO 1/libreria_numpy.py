from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

datos=random.randint(0,10,size=100);

#hist(datos,bins=20);
title("random");
boxplot(datos)
show();
print(datos)