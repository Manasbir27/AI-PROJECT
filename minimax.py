import game_rules
from copy import deepcopy

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    possible_moves = game_rules.get_possible_moves(board.board, 'X' if maximizing_player else 'O')

    if maximizing_player:
        value = float('-inf')
        best_move = None
        for move in possible_moves:
            new_board = deepcopy(board)
            new_board.make_move(move[0], move[1], 'X')
            score, _ = minimax(new_board, depth - 1, alpha, beta, False)
            if score > value:
                value = score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in possible_moves:
            new_board = deepcopy(board)
            new_board.make_move(move[0], move[1], 'O')
            score, _ = minimax(new_board, depth - 1, alpha, beta, True)
            if score < value:
                value = score
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move

def evaluate(board):
    player_score = 0
    opponent_score = 0

    # Scoring mechanism based on factors mentioned in the prompt
    for i in range(8):
        for j in range(8):
            if board.board[i][j] == 'X':
                player_score += get_tile_score(i, j)
            elif board.board[i][j] == 'O':
                opponent_score += get_tile_score(i, j)

    return player_score - opponent_score

def get_tile_score(row, col):
    # Scoring for different positions on the board
    if (row == 0 or row == 7) and (col == 0 or col == 7):
        return 5  # Corner tiles
    elif row == 0 or row == 7 or col == 0 or col == 7:
        return 3  # Edge tiles
    elif (row == 1 or row == 6) and (col == 1 or col == 6):
        return -2  # Next to corners
    elif (row == 0 or row == 7) and (1 <= col <= 6):
        return 1  # Row adjacent to corners
    elif (1 <= row <= 6) and (col == 0 or col == 7):
        return 1  # Column adjacent to corners
    else:
        return 0  # Interior tiles
