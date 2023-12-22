import time

# BackTracking

def is_valid_latin_square(square, n, row, col, num):
    """
    Check if it's valid to place 'num' in the square at (row, col) position.
    """
    for i in range(n):
        if square[row][i] == num or square[i][col] == num:
            return False
    return True

def generate_latin_squares(square, n, row=0, col=0):
    """
    Generate all Latin Squares of order n using backtracking.
    """
    if row == n - 1 and col == n:
        yield [row.copy() for row in square]  # Yield a copy of the square
        return

    if col == n:  # Go to next row
        row += 1
        col = 0

    for num in range(1, n + 1):
        if is_valid_latin_square(square, n, row, col, num):
            square[row][col] = num
            yield from generate_latin_squares(square, n, row, col + 1)
            square[row][col] = 0  # Backtrack

def print_latin_squares(n):
    """
    Print all Latin Squares of order n.
    """
    square = [[0 for _ in range(n)] for _ in range(n)]
    for latin_square in generate_latin_squares(square, n):
        for row in latin_square:
            # print(row)
            pass
    print("done")

# Example usage for n = 3
start_time = time.time()
print_latin_squares(5)
print("--- %s' seconds ---" % (time.time() - start_time))

print("Latin Squares of Order 5:")

