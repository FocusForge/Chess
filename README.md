# ♟️ Chess Board Visualizer

A Python-based ASCII visualizer for a standard 8x8 chess board. This project lays the foundation for building a full chess engine, GUI interface, or game logic system.

## 📌 Features

- Displays a complete chess board with:
  - Initial piece setup for both black and white
  - Column labels (`a` to `h`) and row numbers (`1` to `8`)
- Uses ASCII formatting for clean terminal output
- Modular design for easy expansion

## 🧠 How It Works

- The board is represented as a 2D list (`board`) with each cell containing:
  - `"b_piece"` for black pieces
  - `"w_piece"` for white pieces
  - `""` for empty squares
- The `print_board()` function formats and prints the board with grid lines and labels.

## 🚀 Getting Started

1. Clone the repository or copy the code into a `.py` file.
2. Run the script using Python 3:
   ```bash
   python chess_board.py
