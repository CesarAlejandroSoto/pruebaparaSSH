from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(-pi,pi,0.05);
y=7-7*sin(x);
grid(True);

plot(x,y,"r",label="funcion(1)",linewidth=2);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio a")
legend(title="funciones",loc="upper right",shadow=True,fontsize="large");
show()