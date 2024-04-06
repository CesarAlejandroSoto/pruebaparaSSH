from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(-10,10,1);
y=(x*(x-2))/((x+1)*(x-2));
grid(True);

plot(x,y,"c",label="funcion(4)",linewidth=2);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio d")
legend(title="funciones",loc="lower left",shadow=True,fontsize="large");
show()