import random

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    # Remove some numbers to create the puzzle
    for _ in range(40):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_move_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def is_move_valid(board, row, col, num):
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def user_input(board):
    while True:
        print("\nEnter row, column, and number (e.g., 2 3 4), or 'q' to quit:")
        try:
            user_input = input()
            if user_input.lower() == 'q':
                return
            row, col, num = map(int, user_input.split())
            if is_move_valid(board, row - 1, col - 1, num):
                board[row - 1][col - 1] = num
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Use format 'row column number' (e.g., 2 3 4).")

def print_game(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row)

if __name__ == "__main__":
    sudoku_board = generate_board()
    print("Welcome to Sudoku!")
    print_game(sudoku_board)

    user_input(sudoku_board)

    print("\nSudoku Solved!")
    print_game(sudoku_board)
