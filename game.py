# https://www.codewars.com/kata/67ca09c53513c2e514fdf3d4


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


def input_player_letter(muha):
    player = input(f"{muha} player's letter -> ")
    if player.isalpha():
        return player
    else:
        print("Incorrect! Only letters are allowed.")
        return input_player_letter()


def horizontal(board):
    for line in board:
        for i in range(3):
            if ' ' != line[i] == line[i + 1] == line[i + 2] == line[i + 3]:
                return True


def vertical(board, player):
    for col in range(6):
        for row in range(4):
            if player == board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return True

"""
    +1 row
    +1 col
    1 | s s s       |
    2 | s s s       |
    3 | s s s       |
    4 | s s s       |
    5 |             |
    6 |             |
    7 |             |
       ------------- 
        1 2 3 4 5 6  
    """
def check_d1(board, player):
    
    for row in range(4):
        for col in range(3):
            if player == board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return True


def check_d2(board, player):
    for row in range(3, 7):
        for col in range(3):
            if player == board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return True


def diagonal(board, player):
    if check_d1(board, player):
        return True
    if check_d2(board, player):
        return True


def for_the_win(board, player):
    if horizontal(board) or vertical(board, player) or diagonal(board, player):
        return True
    return False


def place_letter(board, player: str, column: int):
    # [0] ' ' ' ' ' '
    # [1] 'x' ' ' 'x'
    # [2] 'o' ' ' 'o'
    for line in board[::-1]:
        if line[column - 1] == ' ':
            line[column - 1] = player
            print("Assigned")
            return True

    print("This column is full!")
    return False


def player_move(board, player):
    move = input(f"Please select column({player}) -> ")
    if move.isnumeric() and move in ['1', '2', '3', '4', '5', '6']:
        if not place_letter(board, player, int(move)):
            print("Please select an empty column!")
        else:
            return
    else:
        print("Please select one number: 1, 2, 3, 4, 5 or 6!")
    player_move(board, player)


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
        print("Incorrect! Only letters are allowed!")
        return input_player_letter(muha)


player1 = input_player_letter(" First")
player2 = input_player_letter("Second")

# board = [[' '] * COLS] * ROWS

board = [[' ', ' ', ' ', ' ', ' ', ' '], #1
         [' ', ' ', ' ', ' ', ' ', ' '], #2
         [' ', ' ', ' ', ' ', ' ', ' '], #3
         [' ', ' ', ' ', ' ', ' ', ' '], #4
         [' ', ' ', ' ', ' ', ' ', ' '], #5
         [' ', ' ', ' ', ' ', ' ', ' '], #6
         [' ', ' ', ' ', ' ', ' ', ' '],]#7

print_board(board)

while not tie(board):
    player_move(board, player1)
    print_board(board)
    if for_the_win(board, player1):
        print(f"Player {player1} has won!")
        break
    player_move(board, player2)
    print_board(board)
    if for_the_win(board, player2):
        print(f"Player {player2} has won!")
        break
else:
    print(f"It's a tie")

