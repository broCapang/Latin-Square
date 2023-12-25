import numpy as np
import math
import random
import time

# Simulated Annealing for Latin Squares of Order n

def initial_solution(n):
    return [np.random.permutation(n) for _ in range(n)]

def objective_function(grid):
    n = len(grid)
    duplicates = 0
    for i in range(n):
        row_count = [0] * n
        col_count = [0] * n
        for j in range(n):
            row_count[grid[i][j]] += 1
            col_count[grid[j][i]] += 1
        for k in range(n):
            if row_count[k] > 1:
                duplicates += row_count[k] - 1
            if col_count[k] > 1:
                duplicates += col_count[k] - 1
    return duplicates

def neighbor(grid):
    n = len(grid)
    i, j = random.randint(0, n-1), random.randint(0, n-1)
    k, l = random.randint(0, n-1), random.randint(0, n-1)
    new_grid = [row[:] for row in grid]
    new_grid[i][j], new_grid[k][l] = new_grid[k][l], new_grid[i][j]
    return new_grid

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing(n):
    current_solution = initial_solution(n)
    current_cost = objective_function(current_solution)
    temperature = 1.0
    cooling_rate = 0.99
    min_temperature = 0.01

    while temperature > min_temperature:
        new_solution = neighbor(current_solution)
        new_cost = objective_function(new_solution)
        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_solution = new_solution
            current_cost = new_cost
        
        temperature *= cooling_rate

    return current_solution, current_cost

start_time = time.time()
n = 10  # Example size of the Latin Square
solution, cost = simulated_annealing(n)

print("--- %s' seconds ---" % (time.time() - start_time))
for row in solution:
    print(row)
print("Cost:", cost)
