class OthelloBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 'O'
        self.board[3][4] = self.board[4][3] = 'X'

    def display(self):
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")
        print()

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col, player):
            self.board[row][col] = player
            self.flip_tiles(row, col, player)
            return True
        return False

    def is_valid_move(self, row, col, player):
        if not (0 <= row < 8) or not (0 <= col < 8) or self.board[row][col] != ' ':
            return False

        opponent = 'O' if player == 'X' else 'X'

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                    r, c = r + dr, c + dc
                if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                    return True

        return False

    def flip_tiles(self, row, col, player):
        opponent = 'O' if player == 'X' else 'X'

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                to_flip = []
                while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                    to_flip.append((r, c))
                    r, c = r + dr, c + dc
                if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                    for flip_row, flip_col in to_flip:
                        self.board[flip_row][flip_col] = player

    def get_winner(self):
        count_X = sum(row.count('X') for row in self.board)
        count_O = sum(row.count('O') for row in self.board)

        if count_X > count_O:
            return 'X'
        elif count_O > count_X:
            return 'O'
        else:
            return 'Draw'

    def get_score(self, player):
        score = 0
        for row in self.board:
            for tile in row:
                if tile == player:
                    score += 1
        return score

    def is_game_over(self):
        return not any(' ' in row for row in self.board)
