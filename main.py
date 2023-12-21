def print_board(board):
    for row in board:
        print(" | ".join([f'\033[91m{cell}\033[0m' if cell == 'X' else f'\033[94m{cell}\033[0m' if cell == 'O' else cell for cell in row]))
    print("-"*30)


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
    print(f"\033[91m!!! Invalid move, try again.\033[0m")
    print("-"*30)

def tictactoe():
    print("\033[92m========== New Game ==========\033[0m\n" + "-"*30)
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
            print("="*30)
            print_board(board)
            print(f"\033[96m:::::: Player {player} wins! ::::::\033[0m")
            break
        player = "O" if player == "X" else "X"
    


if __name__ == "__main__":
    replay = "y"
    while replay.lower() == "y":
        tictactoe()
        replay = input("Do you want to play again? (y/n): ")