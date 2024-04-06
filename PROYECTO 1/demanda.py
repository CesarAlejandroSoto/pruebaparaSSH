from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

demanda=[7,9,15,10,12];
print(demanda);
hist(demanda,bins=5);
title("prediccio0n demanda")
show();

media=mean(demanda);
print("la media de la demanda es:",media);

estandar=std(demanda);
print("la desviacionn estandar de la demanda es:",estandar);
