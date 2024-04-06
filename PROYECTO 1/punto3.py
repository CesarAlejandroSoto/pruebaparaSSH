from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(0,10,0.05);
y=math.log10(x)/x;
grid(True);

plot(x,y,"y",label="funcion(3)",linewidth=3);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio c")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
show()
