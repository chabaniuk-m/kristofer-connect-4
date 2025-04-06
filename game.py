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
1) Change print_board() to have such output
2) Player 1 choose your symbol: ...   Player 2...
3) They can play by input 1, 2, 3 (number of col to place their symbol)
4) Each time check if somebody won!
5) If board is filled up then it's a tie!
"""


def Print_board(board):
    for line in board:
        print('|', ' '.join(line), sep=' ', end=' |\n')
    print(' ------------- \n  1 2 3 4 5 6  ')


def Horizontal(board, player1, player2):
    for line in board:
        prev = line[0]
        count = 0
        for sym in line:
            if sym == prev:
                count += 1
                if count == 4:
                    return f'{sym}, Won!' # !!!!
            else:
                count = 0
                prev = sym


def Diagonal(board, player1, player2):
    # left-upper corner    to    right-bottom corner 

    #   SIX ↓ FIVE ↓ FOUR ↓ THREE↓  TWO ↓  ONE ↓ ZERO 
  
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
    1 | o           |
    2 |   o         |
    3 | x   o       |
    4 |   x   o     |
    5 |     x o o   |
    6 | x x o x o o |
      -------------
        0 1 2 3 4 5
    """


def Play(board, player, column: int):
    for line in board[::-1]:
        if line [column - 1] == ' ':
            line[column - 1] = player
            return
    print("This column is full!")


player1, player2 = input("First player's name  ->"), input("Second player's name ->")

board = [[' '] * COLS] * ROWS

while Loop:
    ...
