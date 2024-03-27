from copy import deepcopy
import game_rules
import random

class OthelloAgent:
    def __init__(self, player, depth=3):
        self.player = player
        self.depth = depth
        self.stability = [
            [100, -20, 10, 5, 5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [10, -2, -1, -1, -1, -1, -2, 10],
            [5, -2, -1, -1, -1, -1, -2, 5],
            [5, -2, -1, -1, -1, -1, -2, 5],
            [10, -2, -1, -1, -1, -1, -2, 10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10, 5, 5, 10, -20, 100]
        ]

    def get_move(self, board):
        possible_moves = game_rules.get_possible_moves(board.board, self.player)

        # Check if there are possible moves
        if not possible_moves:
            return None

        # Introduce some randomness in move selection
        if random.random() < 0.1:  # Adjust the probability as needed
            return random.choice(possible_moves)
        else:
            best_move = self.minimax(board, self.depth, float('-inf'), float('inf'), True)[1]
            return best_move

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board), None

        possible_moves = game_rules.get_possible_moves(board.board, self.player) if maximizing_player else game_rules.get_possible_moves(board.board, 'O' if self.player == 'X' else 'X')

        if maximizing_player:
            value = float('-inf')
            best_move = None
            for move in possible_moves:
                new_board = deepcopy(board)
                new_board.make_move(move[0], move[1], self.player)
                score, _ = self.minimax(new_board, depth - 1, alpha, beta, False)
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
                new_board.make_move(move[0], move[1], 'O' if self.player == 'X' else 'X')
                score, _ = self.minimax(new_board, depth - 1, alpha, beta, True)
                if score < value:
                    value = score
                    best_move = move
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, best_move

    def evaluate(self, board):
        player_score = 0
        opponent_score = 0

        # Scoring mechanism based on factors mentioned in the prompt
        for i in range(8):
            for j in range(8):
                if board.board[i][j] == self.player:
                    player_score += self.get_tile_score(i, j, board)
                elif board.board[i][j] != ' ':
                    opponent_score += self.get_tile_score(i, j, board)

        # Positive score for the player leading to victory
        if board.get_winner() == self.player:
            player_score += 1000

        return player_score - opponent_score

    def get_tile_score(self, row, col, board):
        # Scoring for different positions on the board
        if (row == 0 or row == 7) and (col == 0 or col == 7):
            return 500  # Corner tiles
        elif row == 0 or row == 7 or col == 0 or col == 7:
            return 100  # Edge tiles
        else:
            # Stability score added
            return self.stability[row][col] + 10 if board.board[row][col] == self.player else 0