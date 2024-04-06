from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=linspace(0,10,20)
y=x-math.sqrt(x);
grid(True);

plot(x,y,"g",label="funcion(2)",linewidth=4);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio b")
legend(title="funciones",loc="upper right",shadow=True,fontsize="medium");
show()