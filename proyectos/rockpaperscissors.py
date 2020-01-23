import random

# Rock, paper, scissors Game by CachesKCH

wins = 0
losses = 0
ties = 0
while True:  # Main loop

    if wins == 0 and losses == 0 and ties == 0:  # Makes sure that this will not show up before first round
        print("ROCK, PAPER, SCISSORS")
        pass
    else:
        print(f"{wins} Wins, {losses} Losses, {ties} Ties.")

    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_input = input().lower()
    game_pool = ["ROCK", "PAPER", "SCISSORS"]
    ai_choice = random.choice(game_pool)
    user_choice = ""  # This line is innecesary but the linter gets mad at me lol

    if user_input == "r":  # Converts user input to full choice names
        user_choice = "ROCK"
    elif user_input == "p":
        user_choice = "PAPER"
    elif user_input == "s":
        user_choice = "SCISSORS"
    elif user_input == "q":  # Quit logic, quits game
        print("see ya next time!")
        break
    else:  # Checks if the user inputs wrong command and restarts de loop
        print("that's not allowed! use a legal command.")
        continue

    print(f"{user_choice} against...")

    # Main game logic
    if ai_choice == user_choice:
        print(f"{ai_choice}! it's a tie!")
        ties += 1
    elif ai_choice == "ROCK" and user_choice == "SCISSORS":
        print(f"{ai_choice}! AI wins!")
        losses += 1
    elif ai_choice == "PAPER" and user_choice == "ROCK":
        print(f"{ai_choice}! AI wins!")
        losses += 1
    elif ai_choice == "SCISSORS" and user_choice == "PAPER":
        print(f"{ai_choice}! AI wins!")
        losses += 1

    elif ai_choice == "ROCK" and user_choice == "PAPER":
        print(f"{ai_choice}! You win!")
        wins += 1
    elif ai_choice == "PAPER" and user_choice == "SCISSORS":
        print(f"{ai_choice}! You win!")
        wins += 1
    elif ai_choice == "SCISSORS" and user_choice == "ROCK":
        print(f"{ai_choice}! You win!")
        wins += 1

print("Thanks for playing!")
