def solve_sudoku(grid):
    """
    Solves a Sudoku grid recursively using backtracking.
    """
    # Find the next empty cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                # Try all possible values for this cell
                for k in range(1, len(grid)+1):
                    if is_valid(grid, i, j, k):
                        # If the value is valid, set it and move on to the next empty cell
                        grid[i][j] = k
                        if solve_sudoku(grid):
                            return True
                        # If the value is not valid, backtrack to the previous cell and try the next value
                        grid[i][j] = 0
                return False
    return True


def is_valid(grid, row, col, value):
    """
    Checks whether a value can be placed in the given cell of the grid.
    """
    # Check row and column for conflicts
    for i in range(len(grid)):
        if grid[row][i] == value or grid[i][col] == value:
            return False
    # Check box for conflicts
    box_size = int(len(grid)**0.5)
    box_row = (row // box_size) * box_size
    box_col = (col // box_size) * box_size
    for i in range(box_size):
        for j in range(box_size):
            if grid[box_row+i][box_col+j] == value:
                return False
    return True
