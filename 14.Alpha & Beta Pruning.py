import math

# Constants for the players
HUMAN = -1
COMP = +1

# The board cells
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# This function prints the board
def print_board(board):
    chars = {0: ' ', HUMAN: 'X', COMP: 'O'}
    for row in board:
        for cell in row:
            print(f"{chars[cell]}", end="|")
        print()
        print("-----")

# This function checks for empty cells
def empty_cells(board):
    cells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells

# This function checks if the board is full
def is_full(board):
    return not any(0 in row for row in board)

# This function checks if a player has won
def evaluate(state):
    if wins(state, COMP):
        return +1
    elif wins(state, HUMAN):
        return -1
    else:
        return 0

# This function checks if a move is valid
def valid_move(x, y):
    return [x, y] in empty_cells(board)

# This function makes a move
def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False

# This function checks for winning condition
def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state

# Alpha-Beta Pruning algorithm
def alpha_beta(state, depth, alpha, beta, player):
    if wins(state, COMP):
        return +1
    elif wins(state, HUMAN):
        return -1
    elif is_full(state) or depth == 0:
        return 0

    if player == COMP:
        max_eval = -math.inf
        for cell in empty_cells(state):
            x, y = cell
            state[x][y] = COMP
            eval = alpha_beta(state, depth - 1, alpha, beta, HUMAN)
            state[x][y] = 0
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for cell in empty_cells(state):
            x, y = cell
            state[x][y] = HUMAN
            eval = alpha_beta(state, depth - 1, alpha, beta, COMP)
            state[x][y] = 0
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# This function makes the best move for the AI
def ai_turn():
    best_move = (-1, -1)
    best_value = -math.inf
    for cell in empty_cells(board):
        x, y = cell
        board[x][y] = COMP
        move_value = alpha_beta(board, len(empty_cells(board)), -math.inf, math.inf, HUMAN)
        board[x][y] = 0
        if move_value > best_value:
            best_value = move_value
            best_move = (x, y)
    if best_move != (-1, -1):
        set_move(best_move[0], best_move[1], COMP)

# This function starts the game
def play():
    while len(empty_cells(board)) > 0 and not wins(board, HUMAN) and not wins(board, COMP):
        print_board(board)
        x = int(input("Enter the row (0, 1, 2): "))
        y = int(input("Enter the column (0, 1, 2): "))
        if not valid_move(x, y):
            print("Invalid move. Try again.")
            continue
        set_move(x, y, HUMAN)
        if not (wins(board, HUMAN) or is_full(board)):
            ai_turn()

    print_board(board)

    if wins(board, HUMAN):
        print("HUMAN wins!")
    elif wins(board, COMP):
        print("COMP wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play()
