from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(-10,20,0.005);
y=x/e**abs(x-1);
grid(True);

plot(x,y,"r",label="funcion(6)",linewidth=7);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio f")
legend(title="funciones",loc="lower right",shadow=True,fontsize="medium");
show()