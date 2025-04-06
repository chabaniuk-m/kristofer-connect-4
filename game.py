ROWS = 7
COLS = 6

"""
|             |
|             |
|             |
|             |
|             |
|       o     |
| x x o x o o |
 -------------
  1 2 3 4 5 6

Task:
1) ✅ Change print_board() to have such output
2) ✅ Player 1 choose your symbol: ...   Player 2...
3) They can play by input 1, 2, 3 (number of col to place their symbol)
4) Each time check if somebody won!
5) If board is filled up then it's a tie!
"""


def print_board(board):
    for line in board:
        print('|', ' '.join(line), sep=' ', end=' |\n')
    print(' ------------- \n  1 2 3 4 5 6  ')


def horizontal(board, player):
    for line in board:
        prev = player
        count = 0
        for sym in line:
            if sym == prev:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
                prev = sym


def diagonal(board, player):
    # left-upper corner    to    right-bottom corner 

    # [6][3] [5][2] [4][1] [3][0]
    # [6][4] [5][3] [4][2] [3][1] [2][0]
    # [6][5] [5][4] [4][3] [3][2] [2][1] [1][0]
    # [6][6] [5][5] [4][4] [3][3] [2][2] [1][1] [2][0] 

    # [5][3] [4][2] [3][1] [2][0]
    # [5][4] [4][3] [3][2] [2][1] [2][0]
    # [5][5] [4][4] [3][3] [2][2] [2][1] [2][0]
    # [5][6] [4][5] [3][4] [2][3] [2][2] [2][1] [2][0]

    # [4][3] [3][2] [2][1] [1][0]
    # [4][4] [3][3] [2][2] [1][1] [0][0]
    # [4][5] [3][4] [2][3] [1][2] [0][1]
    # [4][6] [3][5] [2][4] [1][3] [0][2]
    """
    0 |             |
    1 | o       x   |
    2 |   o   x     |
    3 | x   x       |
    4 |   x   o     |
    5 |     x x o   |
    6 | x x o x x o |
      ---------------
        0 1 2 3 4 5
    """

def for_the_win(board, player):
    if horizontal(board, player) or diagonal(board, player):
        return True
    return False


def place_letter(board, player, column: int):
    for line in board[::-1]:
        if line [column - 1] == ' ':
            line[column - 1] = player
            return True
    print("This column is full!")
    return False


def player_move(board, player):
    move = input("Please select column -> ")
    if not move.isalpha() or move in range(1, 7):
        if not place_letter(board, player, int(move)):
            print("Please select an empty column!")
            return player_move
    else:
        print("Please select one number, 1, 2, 3, 4, 5 or 6!")
    return player_move()


def tie(board):
    for line in board:
        if ' ' in line:
            return False
    return True


def input_player_letter(muha):
    player = input(f"{muha} player's letter -> ")
    if player.isalpha():
        return player
    else:
        print("Incorrect! Only letters are allowed.")
        return input_player_letter()


player1 = input_player_letter(" First")
player2 = input_player_letter("Second")

board = [[' '] * COLS] * ROWS

while not tie():
    place_letter(board, player1)
    print_board(board)
    horizontal()

