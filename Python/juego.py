import random

print("¡Bienvenido al juego de adivinanza de números!")
numero_secreto = random.randint(1, 20)

for intentos in range(1, 7):
    print("Intento número " + str(intentos))
    numero_usuario = int(input("Adivina el número (entre 1 y 20): "))
    
    if numero_usuario < numero_secreto:
        print("El número es demasiado bajo.")
    elif numero_usuario > numero_secreto:
        print("El número es demasiado alto.")
    else:
        break

if numero_usuario == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número en " + str(intentos) + " intentos!")
else:
    print("Lo siento, el número era " + str(numero_secreto) + ". ¡Mejor suerte la próxima vez!")
