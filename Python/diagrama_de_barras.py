from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

productos=["producto A","producto B","producto C"];
ventas=[125000,530000,650000];
bar(productos,ventas);
title("grafica de ventas de productos");
xlabel("nombre de los productos");
ylabel("ventas del producto");
show();
