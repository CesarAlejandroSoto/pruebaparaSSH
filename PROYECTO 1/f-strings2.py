from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*
'''
x=[1,2,3,4,5];
y=[6,8,9,10,11];

plot(x,y);
text(3,6,"punto importante",fontsize=16,color="red",fontweight="bold",fontstyle="italic");
show();'''

#x=linspace(-10,10,1000);
x=arange(-10,10,0.05);
y=sin(x);
y1=cos(x);

subplot(2,1,1)
plot(x,y,"r--",label="seno",linewidth=4);
xlabel("ejex")
ylabel("eje y")
title("grafica del seno")
subplot(2,1,2)
plot(x,y1,"y",label="coseno");
legend(title="funciones",loc="upper left",shadow=True,fontsize="medium");

xlabel("soto");
ylabel("cesar");
title("funcion seno y coseno");
text(0.1,0.2,"alejandro",fontsize=16,color="red",fontweight="bold",fontstyle="italic");
show();