from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

x=linspace(-10,10,1000)
y=x*(x**2+4)**2;
grid(True);

plot(x,y,"b",label="funcion(1)",linewidth=2);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio a")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
show()