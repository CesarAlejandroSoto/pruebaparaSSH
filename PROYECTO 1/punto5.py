from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=linspace(-100,100,500)
y=sin(1/x);
grid(True);

plot(x,y,"m",label="funcion(5)",linewidth=6);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio e")
legend(title="funciones",loc="lower left",shadow=True,fontsize="medium");
show()