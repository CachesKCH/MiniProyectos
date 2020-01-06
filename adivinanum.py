import random

secret_num = random.randint(0, 100)  # Genera un numero aleatorio y lo guarda en la variable secret_num
guess = int(input("Adivina el numero: "))  # Guarda un numero dado por el usuario y lo guarda en la variable guess
wants_exit = False

while not wants_exit:
    if secret_num == guess:  # Compara las variables y comprueba si el usuario adivino el numero
        print("Ganaste!")
    else:
        print("Perdiste! el numero era " + str(secret_num))
# print(secret_num)
