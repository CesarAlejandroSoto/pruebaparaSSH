from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(-pi,pi,0.015);
y=3-6*sin(x);
grid(True);

plot(x,y,"g",label="funcion(2)",linewidth=4);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio b")
legend(title="funciones",loc="upper right",shadow=True,fontsize="large");
show()