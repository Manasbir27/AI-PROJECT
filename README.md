# Othello AI

Othello, also known as Reversi, is a classic two-player strategy board game. This implementation provides an AI agent that utilizes the Minimax algorithm with Alpha-Beta pruning to play against a human player. The AI agent evaluates the board positions using a sophisticated scoring mechanism tailored for Othello, which considers factors such as maximizing interior disks, minimizing frontier disks, maximizing stable disks, acquiring corners, and more.

## Features

- Graphical User Interface (GUI) for playing Othello against the AI agent.
- Implementation of the Minimax algorithm with Alpha-Beta pruning for the AI agent.
- Optimized move selection using a scoring mechanism specific to Othello.
- Simulation of the game loop, alternating between the AI agent and the human player.
- Determination of the winner based on the game's rules.
- Random move selection with a small probability to introduce variability in the AI's gameplay.

## Files

1. `agent.py`: Contains the implementation of the `OthelloAgent` class, which uses the Minimax algorithm to decide the next move for the AI player.
2. `game_rules.py`: Includes helper functions for checking valid moves and flipping tiles on the board.
3. `main.py`: Provides a graphical user interface (GUI) for playing Othello against the AI agent.
4. `minimax.py`: Implements the Minimax algorithm with Alpha-Beta pruning and the evaluation function for scoring board positions.
5. `othello.py`: Defines the `OthelloBoard` class, which represents the game board and handles moves and board evaluation.

## How to Run

1. Make sure you have Python installed on your system.
2. Run the `main.py` file to start the GUI:

3. The GUI window will open, displaying the Othello board.
4. Click the "Next Move" button to make the AI agent's move. The game will alternate between the AI agent and the human player.
5. The game will continue until it reaches a terminal state (a winner is declared or a draw occurs).

## Algorithm and Scoring Mechanism

The `OthelloAgent` class implements the Minimax algorithm with Alpha-Beta pruning to decide the best move for the AI player. The algorithm explores the game tree up to a specified depth, evaluating each move using the `evaluate` function.

The `evaluate` function assigns a score to a given board state for a specific player, considering the following factors:

- Corner tiles: Highest score, as they are strategic positions.
- Edge tiles: High score, as they provide control over the board.
- Tiles adjacent to corners: Negative score, as they can be vulnerable positions.
- Stability score: A predefined weight matrix is used to score positions based on their stability.
- Leading to victory: A large bonus score is added if the board state leads to victory for the player.

The agent also introduces some randomness in move selection with a small probability to add variability in its gameplay.

## Optimization

To optimize memory usage, the implementation employs the following strategies:

- Transposition Tables: Store previously computed positions along with their evaluations to avoid redundant computations.
- Iterative Deepening: Gradually increase the search depth, reusing the results of shallower searches at deeper levels.
- Dynamic Memory Allocation: Allocate memory dynamically for data structures that vary in size during execution.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
