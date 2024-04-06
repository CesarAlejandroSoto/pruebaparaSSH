from numpy import *#importa la libreria numpy
from matplotlib.pyplot import *

import numpy as np
vector=array([2,2,3,6,5]);
print("la posicion es:",vector[4]);
print("el valor mas grande del vector es: ",max(vector));
print("el valor mas pequeño del vector es: ",min(vector));

print("la media es:",mean(vector));
plot(vector);
show();
