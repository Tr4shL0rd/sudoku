from solve import solve_sudoku
from generate import generate_sudoku_grid

generate_sudoku_grid(grid_size=9, output_name="sudoku.txt", readable=False)
# Read the grid from file
with open("sudoku.txt", "r") as f:
    grid_text = f.read()

# Convert the grid to a 2D list of integers
grid = []
for line in grid_text.split("\n"):
    row = []
    for c in line:
        if c.isdigit():
            row.append(int(c))
    if row:
        grid.append(row)

# Solve the grid
solve_sudoku(grid)

# Print the solved grid
print("Solved Grid:")
for row in grid:
    print(row)
