#####################
# Welcome to Cursor #
#####################

"""
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
"""

'''
Make first number col, second row
Add option to replay game
Stop moves from being overwritten

Add Validation
'''

# Generate me a CLI-based game of TicTacToe
def print_board(board):
    for index, row in enumerate(board):
        print(" | ".join(row))
        # if index != len(board)-1:
        #     print("-"*9)
    print("-"*33)


def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def error_message():
    print("!!! Invalid move, try again.")
    print("-"*33)

def tictactoe():
    print("New Game =====\n" + "-"*33)
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    invalid = False
    while True:
        if not invalid:
            print_board(board)
        print(f"- Player {player} turn")
        move = input("Enter your move (col row): ")
        input_move = [int(char)-1 for char in move if char.isdigit() and 0 <= int(char)-1 <= 2]

        if len(move) != 2 or len(input_move) != 2:
            error_message()
            invalid = True
            continue

        col, row = input_move[0], input_move[1]
        if board[row][col]  != " ":
            error_message()
            invalid = True
            continue

        board[row][col] = player
        invalid = False
        if check_win(board):
            print("="*33)
            print(f"::: Player {player} wins! :::")
            break
        player = "O" if player == "X" else "X"
    


if __name__ == "__main__":
    tictactoe()
    replay = input("Do you want to play again? (y/n): ")
    if replay.lower() == "y":
        tictactoe()