from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=linspace(-pi,pi,1000)
y=math.sqrt(5*cos(2*x));
grid(True);

plot(x,y,"b",label="funcion(5)",linewidth=7);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio e")
legend(title="funciones",loc="lower right",shadow=True,fontsize="medium");
show()