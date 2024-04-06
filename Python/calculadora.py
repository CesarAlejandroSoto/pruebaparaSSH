# Función para realizar la suma
def sumar(x, y):
    return x + y

# Función para realizar la resta
def restar(x, y):
    return x - y

# Función para realizar la multiplicación
def multiplicar(x, y):
    return x * y

# Función para realizar la división
def dividir(x, y):
    return x / y

print("¡Bienvenido a la calculadora!")

while True:
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Pedir la entrada del usuario
    opcion = input("Ingresa la opción (1/2/3/4): ")

    # Verificar la opción ingresada por el usuario
    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print(num1, "+", num2, "=", sumar(num1, num2))

        elif opcion == '2':
            print(num1, "-", num2, "=", restar(num1, num2))

        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif opcion == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
