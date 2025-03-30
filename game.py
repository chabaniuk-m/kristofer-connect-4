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


def print_board(board):
    print(*board, sep='\n')


board = [[' '] * COLS] * ROWS

print_board(board)
