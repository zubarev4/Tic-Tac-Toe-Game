# Tic-Tac-Toe (Python)

This is a simple **Tic-Tac-Toe** game implemented in Python. The game is played in the console, allowing two players to take turns placing their marks on a 3x3 grid.

## How to Play

1. Run the script in a Python environment.
2. Choose whether to be **Player 1 (X)** or **Player 2 (O)**.
3. Players take turns choosing a position (1-9) to place their marker.
4. The game checks for a **win** or **tie** after every move.
5. The game ends when a player wins or the board is full.

## Game Board Layout

The board positions are numbered as follows:

```
 7 | 8 | 9
-----------
 4 | 5 | 6
-----------
 1 | 2 | 3
```

## Code Overview

The game consists of the following functions:

- `display(board)`: Displays the current state of the board.
- `player_info()`: Asks the user to choose their marker (X or O).
- `player_turn(board, player)`: Allows a player to place their marker on the board.
- `check_win(board, player)`: Checks if a player has won the game.
- `check_tie(board)`: Checks if the board is full, resulting in a tie.

## Requirements

- Python 3.x
- No external libraries required

## Running the Game

To run the game, execute the following command in your terminal:

```bash
python tic_tac_toe.py
```

