board = [
    # Black pieces
    ["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
    ["b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn"],
    # Empty rows
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    # White pieces
    ["w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn"],
    ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"],
]

def print_board(board):
    print("    a   b   c   d   e   f   g   h")
    print("  " + "-" * 33)
    for i, row in enumerate(board, start=1):
        print(f"{i} | " + " | ".join(piece if piece else " " for piece in row) + " |")
        print("  " + "-" * 33)

# Call the function to display the board
print_board(board)