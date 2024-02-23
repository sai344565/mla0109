import math
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def evaluate(board):
    for row in board:
        if row.count('X') == 3:
            return 10
        elif row.count('O') == 3:
            return -10
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 10
        elif all(board[row][col] == 'O' for row in range(3)):
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 10
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -10
    return 0  
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if is_board_full(board):
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  
        return min_eval
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        print("Player X's turn")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if is_valid_move(board, row, col):
            board[row][col] = 'X'
            if evaluate(board) == 10:
                print_board(board)
                print("Player X wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            print_board(board)
            print("Player O's turn")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = 'O'
            if evaluate(board) == -10:
                print_board(board)
                print("Player O wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
