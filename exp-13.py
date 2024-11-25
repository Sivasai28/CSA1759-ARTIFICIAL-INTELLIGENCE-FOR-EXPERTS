import math

# Define the player and opponent
PLAYER = "X"
OPPONENT = "O"

# Function to check if any player has won
def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return 10 if row[0] == PLAYER else -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return 10 if board[0][col] == PLAYER else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == PLAYER else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == PLAYER else -10

    # No winner
    return 0

# Check if moves are remaining
def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If the maximizer has won
    if score == 10:
        return score - depth

    # If the minimizer has won
    if score == -10:
        return score + depth

    # If no moves are left, it's a tie
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best

# Function to find the best move for the current player
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = "_"
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Example usage
if __name__ == "__main__":
    # Example Tic-Tac-Toe board
    board = [
        ["X", "O", "X"],
        ["_", "O", "_"],
        ["_", "_", "_"]
    ]

    best_move = find_best_move(board)
    print("The best move is:", best_move)

