def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None
def minimax(board, depth, maximizing_player):
    score = evaluate(board)
    if score is not None:
        return score
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if is_valid_move(board, i, j):
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '  
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if is_valid_move(board, i, j):
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '  
                    min_eval = min(min_eval, eval)
        return min_eval
def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if is_valid_move(board, i, j):
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
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
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            print_board(board)
            print("Player O's turn")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = 'O'
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
        else:
            print("Invalid move. Try again.")
if __name__ == "__main__":
    play_tic_tac_toe()
