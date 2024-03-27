def is_valid_move(board, row, col, player):
    if not (0 <= row < 8) or not (0 <= col < 8) or board[row][col] != ' ':
        return False

    opponent = 'O' if player == 'X' else 'X'

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                r, c = r + dr, c + dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                return True

    return False

def get_possible_moves(board, player):
    possible_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, row, col, player):
                possible_moves.append((row, col))
    return possible_moves

def flip_tiles(board, row, col, player):
    opponent = 'O' if player == 'X' else 'X'

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                to_flip.append((r, c))
                r, c = r + dr, c + dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                for flip_row, flip_col in to_flip:
                    board[flip_row][flip_col] = player