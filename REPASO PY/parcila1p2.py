'''Diseñar un programa que implemente una agenda telefónica (Implementar el programa con un 
diccionario)
En la agenda se podrán guardar nombres y números de teléfono. El programa nos debe 
mostrar el siguiente menú:
• Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar 
el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se 
encuentra, debe permitir ingresar el nuevo nombre con el teléfono correspondiente.
• Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres 
comiencen por dicha cadena.
• Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
• Listar: Nos muestra todos los contactos de la agenda.'''

agenda={}; #TERMINAR

while True:
    print("1. Añadir un contacto \n 2. Modificar un contacto \n 3. Buscar contacto \n 4. Eliminar contactos \n 5. Mostrar contactos: ");
    opcion = int(input("Que opcion desea ejecutar: "))
    
    if opcion == 1:
        nuevo_contacto=str(input("Digite el nombre del contacto que desea agregar: "));
        nuevo_numero=int(input("Digite el numero del contacto que desea agregar: "));
        agenda.setdefault(nuevo_contacto,nuevo_numero);
    elif opcion == 2:
        modificar_nombre = str(input("que nombre de contacto desea modificar :"));
        modificar_numero = int(input("que numero de contacto desea modificar :"));
        agenda[modificar_nombre]=nuevo_numero;
        agenda[nuevo_contacto]=modificar_numero;
    elif opcion == 3:
        buscar_contacto = str(input("que contacto desea buscar : "))
        agenda[buscar_contacto];
    elif opcion == 4:
        eliminar_contacto = str(input("que contacto desea eliminar :"))
        del(agenda[eliminar_contacto]);
    elif opcion == 4:
        agenda.items();
        print("los contactos de la agenda son :");

               
    print(agenda);
            
