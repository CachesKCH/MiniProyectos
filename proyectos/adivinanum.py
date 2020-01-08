import random

# Variables globales que mantienen la informacion que genera el loop
wants_exit = False
start_msg = False
points = 0


# Funcion que recibe la entrada del usuario y decide si es un comando o numero legal
def command_checker(guess_var):
    try:
        if isinstance(int(guess_var), int):
            input_is_legal = True
            return input_is_legal
    except ValueError:
        if (guess_var == "PUNTOS") or (guess_var == "SALIR"):
            input_is_legal = True
        else:
            input_is_legal = False
        return input_is_legal


while not wants_exit:

    # Explica el juego, como salir y como ver puntos
    if start_msg is False:
        print("Este juego genera un numero del 1 al 100, tu trabajo es adivinarlo. tienes 5 intentos, suerte!")
        print("Para salir escribe 'SALIR', para ver tus puntos escribe 'PUNTOS'.")
        start_msg = True
    elif start_msg is True:  # Mensaje que se muestra luego de jugar al menos una vez
        print("Generando nuevo numero...")  # En realidad es instantaneo, puse esto para hacer un 'separador'
        print("...")
        print("...")
        print("...")
        print("...")
        print("...")
        print("...")

    # Variables locales que se regeneran cuando el programa termina de ejecutar la logica principal
    secret_num = random.randint(0, 100)  # Genera un numero aleatorio y lo guarda en la variable secret_num
    tries_left = 5

    while tries_left > 0:  # Logica principal del juego

        guess = input("Adivina el numero: ")  # Guarda el numero dado por el usuario en la variable guess
        guess = guess.upper()

        # Codigo que comprueba si la entrada del usuario es un comando existente
        is_legal = command_checker(guess)
        if is_legal is True:
            pass
        else:
            print("El comando " + guess + " no existe. por favor inserte un numero o comando existente")
            break

        # Logica para el comando 'SALIR' y el comando 'PUNTOS'
        try:
            if isinstance(int(guess), int):
                pass
        except ValueError:
            if guess == "SALIR":
                wants_exit = True
                break
            elif guess == "PUNTOS":
                print("Tienes " + str(points) + " puntos")
                break

        # Compara las variables y comprueba si el usuario adivino el numero
        if str(secret_num) == guess:  # Si son iguales el programa suma un punto y sale del loop
            points += 1
            print("Ganaste!")
            break
        elif secret_num != guess and tries_left == 1:  # Si fallas los intentos imprime secret_num y sale del loop
            tries_left += -1
            print("Perdiste! el numero era " + str(secret_num))
            break
        elif secret_num != guess and tries_left == 2:  # Cambia el texto a 'intento'
            tries_left += -1
            print("Mal! te queda " + str(tries_left) + " intento")
        elif secret_num != guess:  # Si no son iguales suma 1 a 'tries' e imprime la cantidad de intentos que sobran
            tries_left += -1
            print("Mal! te quedan " + str(tries_left) + " intentos")

print("Gracias por jugar!")
