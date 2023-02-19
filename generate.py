from asyncore import read
import random

def get_num_horizontal_boxes(grid_size):
    """
    Returns the number of horizontal boxes in a Sudoku grid of the given size.
    """
    box_size = int(grid_size ** 0.5)
    num_horizontal_boxes = grid_size // box_size
    return num_horizontal_boxes

def generate_sudoku_grid(grid_size:int, output_name:str="sudoku.txt", readable:bool=True):
    """
    Generates a Sudoku grid of the given size.
    """
    # Compute the number of boxes in each row and column
    box_size = int(grid_size ** 0.5)
    
    # Compute the separator length
    sep_len = box_size * 2 + 1
    
    # Generate a blank grid
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Fill the main diagonal with random values
    for i in range(grid_size):
        value = i % box_size + 1
        grid[i][i] = value
    
    # Shuffle the values in each box
    for i in range(box_size):
        for j in range(box_size):
            box_values = list(range(1, box_size + 1))
            random.shuffle(box_values)
            for k in range(box_size):
                row = i * box_size + k
                col = j * box_size + k
                grid[row][col] = box_values[k]
    
    # Shuffle the rows and columns within each row and column box
    for i in range(grid_size):
        row_box = i // box_size
        col_box = i % box_size
        row_start = row_box * box_size
        col_start = col_box * box_size
        row_indices = list(range(row_start, row_start + box_size))
        col_indices = list(range(col_start, col_start + box_size))
        random.shuffle(row_indices)
        random.shuffle(col_indices)
        for j in range(box_size):
            row = row_indices[j]
            for k in range(box_size):
                col = col_indices[k]
                if j != k:
                    grid[row][col], grid[row_indices[k]][col_indices[j]] = grid[row_indices[k]][col_indices[j]], grid[row][col]
    
    # Convert the grid to text
    grid_text = ""
    for i in range(grid_size):
        for j in range(grid_size):
            grid_text += str(grid[i][j])
            if j != grid_size - 1:
                if (j + 1) % box_size == 0:
                    #pass
                    grid_text += " | " if readable else " "
                else:
                    grid_text += " "
        if i != grid_size - 1:
            grid_text += "\n"
            if (i + 1) % box_size == 0:
                #pass
                if readable:
                    grid_text += "-" * (1+sep_len*get_num_horizontal_boxes(grid_size)) + "\n"
                
    # Write the grid to a file
    with open(output_name, "w") as f:
        f.write(grid_text)
# Example usage
