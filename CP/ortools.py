from ortools.sat.python import cp_model
import time

# OR-Tools

def solve_latin_square_or_tools(n):
    model = cp_model.CpModel()
    square = [[model.NewIntVar(1, n, f'square_{i}_{j}') for j in range(n)] for i in range(n)]

    # Adding constraints for rows and columns
    for i in range(n):
        model.AddAllDifferent(square[i])  # Row constraints
        model.AddAllDifferent([square[j][i] for j in range(n)])  # Column constraints

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    print(status)

    if status == cp_model.OPTIMAL:
        for row in square:
            print([solver.Value(cell) for cell in row])

# Example usage
start_time = time.time()
solve_latin_square_or_tools(10)
print("--- %s' seconds ---" % (time.time() - start_time))

