import random
import math
import time

# Simulated Annealing

def is_valid_latin_square(square, n):
    # Check for any repeated numbers in rows or columns
    for i in range(n):
        if len(set(square[i])) < n or len(set(row[i] for row in square)) < n:
            return False
    return True

def calculate_violations(square, n):
    # Calculate the number of constraint violations
    violations = 0
    for i in range(n):
        row_violations = n - len(set(square[i]))
        col_violations = n - len(set(row[i] for row in square))
        violations += row_violations + col_violations
    return violations

def generate_random_latin_square(n):
    square = [[(i + j) % n + 1 for i in range(n)] for j in range(n)]
    random.shuffle(square)
    for row in square:
        random.shuffle(row)
    return square

def simulated_annealing_latin_square(n):
    current_square = generate_random_latin_square(n)
    current_cost = calculate_violations(current_square, n)

    temp = 1.0
    temp_min = 0.00001
    alpha = 0.99

    while temp > temp_min:
        i = 0
        while i <= 100:
            new_square = [row[:] for row in current_square]
            row = random.randint(0, n - 1)
            col1, col2 = random.sample(range(n), 2)
            new_square[row][col1], new_square[row][col2] = new_square[row][col2], new_square[row][col1]

            new_cost = calculate_violations(new_square, n)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_square = new_square
                current_cost = new_cost

            i += 1
        temp *= alpha

    return current_square, current_cost

# Solve for a 3x3 Latin Square
n = 10
start_time = time.time()
solution, cost = simulated_annealing_latin_square(n)
print("--- %s' seconds ---" % (time.time() - start_time))
# print(f"Solution (Cost: {cost}):")
# for row in solution:
#     print(row)
