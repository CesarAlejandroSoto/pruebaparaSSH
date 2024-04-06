from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

meses=["enero","febrero","marzo","abril"];
gastos=[250000,560000,52000,690000];
pie(gastos,labels=meses,autopct="%1.1f%%");
title("gastos mensuales");
show()