game = [[2, 0, 1],  # Tablero del juego
        [0, 0, 0],
        [2, 0, 0]]

for col in range(len(game)):
    check = []
    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("Winner")


# def win(current_game):
#     for row in game:
#         print(row)
#         if row.count(row[0]) == len(row) and row[0] != 0:
#             print("Winner")
#
#
# win(game)












# def game_board(game_map, player=0, row=0, column=0, just_display=False):
#     try:
#         print("   A  B  C")
#         if not just_display:
#             game_map[row][column] = player
#         for count, row in enumerate(game_map):
#             print(count, row)
#     except IndexError as e:
#         print("Error: did you input row/column as 0 1 or 2 ?", e)
#     except Exception as e:
#         print("something went very wrong!", e)
#
#
# game_board(game, just_display=True)
# game_board(game_board, player=1, row=2, column=1)
