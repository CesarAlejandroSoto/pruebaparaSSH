from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
import math

x=arange(-pi,2*pi,0.01);
y=sin(x);
z=cos(x);
t=exp(-x);
v=x**2;
grid(True);

subplot(2,2,1)
plot(x,y,"m",label="funcion(1)",linewidth=6);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio a")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
subplot(2,2,2)
plot(x,z,"r",label="funcion(2)",linewidth=6);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio b")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
subplot(2,2,3)
plot(x,t,"b",label="funcion(3)",linewidth=6);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio c")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
subplot(2,2,4)
plot(x,v,"r",label="funcion(4)",linewidth=6);
xlabel("eje x")
ylabel("eje y")
title("grafica ejercicio d")
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");
show()