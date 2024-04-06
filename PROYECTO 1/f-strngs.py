from numpy import *#importa la libreria numpy
from matplotlib.pyplot import*

nombre="mario";
sueldo= 1_000_000;
sueldo1= 150.4544;
#mensaje=f"el valor del sueldo con decimales es {sueldo1:.2f}";

#print(mensaje);
valor_formateado="${:,.2f}".format(sueldo1);
print(valor_formateado);

print(f"el valor del sueldo es ${sueldo1:,.2f}");

print("el nombre de la persona es :",nombre,"es genero masculino",sueldo);

print(f"el nombre de la persona es {nombre} es genero masculino su sueldo es {sueldo}");
