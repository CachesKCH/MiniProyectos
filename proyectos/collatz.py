def collatz(num):
    """Recieves an integer as an attribute, if the number is even it divides it by two and
    returns the result. if the number is odd, it converts it to even and returns the result.
    """
    if num % 2 == 0:
        result = num / 2
        print(result)
    else:
        result = 3 * num + 1
        print(result)
    return result


def main_game():
    """Main game loop. it prompts the user to input a number wich is saved inside base_num,
    converts the number and checks if the input was actually an integer. if the input is
    indeed a number it loops through collatz until base_num reaches 1 and breaks the loop."""
    first_time_message = False
    while True:

        if not first_time_message:  # This makes sure the greet message shows up only one time.
            print("This algorithm will process any number you input until it reaches 1.")
            first_time_message = True

        print("Input a number:")

        try:
            base_num = int(input(""))

        except ValueError:
            print("Only numbers allowed")
            continue

        while base_num != 1:

            base_num = collatz(base_num)


main_game()
