from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=linspace(-pi,pi,1000)
y=cos(8*x);
grid(True);

plot(x,y,"c",label="funcion(4)",linewidth=3);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio d")
legend(title="funciones",loc="lower left",shadow=True,fontsize="medium");
show()