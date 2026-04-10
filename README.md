# Tic Tac Toe AI

A tic-tac-toe game where you play versus the AI which utilizes the minimax algorithm to play optimal moves. The house always wins.

An unbeatable Tic Tac Toe game featuring an AI opponent that uses the minimax algorithm to guarantee optimal play. The AI will never lose and will win whenever possible.

## Description

This project implements a classic Tic Tac Toe game with an AI player powered by the minimax algorithm. The minimax algorithm explores all possible game states to choose the best move, ensuring the AI plays perfectly. As a result, the AI will always win or tie against any human opponent.

The game includes:
- A graphical user interface built with Pygame
- Optimal AI decision-making using minimax
- Player choice between X and O
- Game restart functionality

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually:

   ```bash
   pip install pygame
   ```

## Usage

Run the game using the runner script:

```bash
python runner.py
```

### How to Play

1. Launch the game.
2. Select whether you want to play as X or O by clicking the corresponding button.
3. The game board will appear.
4. Click on an empty square to make your move.
5. The AI will respond automatically.
6. The game ends when someone wins or it's a tie.
7. Click "Play Again" to start a new game.

## Algorithm Explanation

The AI uses the **minimax algorithm** to determine the best move:

- **Max Player (AI)**: Tries to maximize the score (win = 1, tie = 0, loss = -1)
- **Min Player (Human)**: Assumes the opponent will minimize the AI's score
- The algorithm recursively explores the game tree, evaluating terminal states
- Returns the optimal action for the current player

This ensures the AI plays perfectly and cannot be beaten.

## File Structure

- `tictactoe.py`: Contains the game logic, minimax algorithm, and helper functions
- `runner.py`: Pygame-based GUI for playing the game
- `requirements.txt`: Lists the Python dependencies (Pygame)
- `OpenSans-Regular.ttf`: Font file used by the GUI
- `readme.md`: This file
- `__pycache__/`: Python bytecode cache (auto-generated)

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is for educational purposes.
