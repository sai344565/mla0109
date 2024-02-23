import random

def objective_function(x):
    return -(x**2)

def hill_climbing(max_iter=100, step_size=0.1):
    current_solution = random.uniform(-10, 10)

    for _ in range(max_iter):
        current_value = objective_function(current_solution)
        next_solution = current_solution + random.uniform(-step_size, step_size)

        if objective_function(next_solution) > current_value:
            current_solution = next_solution

    return current_solution, objective_function(current_solution)
best_solution, best_value = hill_climbing()

print(f"Best Solution: {best_solution}")
print(f"Best Value: {best_value}")
