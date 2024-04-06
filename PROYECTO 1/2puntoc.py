from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(-pi,pi,0.070);
y=sin(6*x);
grid(True);

plot(x,y,"m",label="funcion(3)",linewidth=6);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio c")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
show()