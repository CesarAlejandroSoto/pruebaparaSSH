archivo_texto = open("texto1.txt",'r');

leer_archivo = archivo_texto.read();



print(leer_archivo);






archivo_texto.close();


texto_adicional= str(input("digite un texto que desee agregar"));
texto_adicional2 = "343434343434343434343434343434343434";

permiso_archivo = open("texto1.txt",'a');
permiso_archivo.write("\n" + texto_adicional + "\n" + texto_adicional2);
permiso_archivo.close();