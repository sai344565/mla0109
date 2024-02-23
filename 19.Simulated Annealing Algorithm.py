import math
import random
def objective_function(x):
    return x**2 + 5*math.sin(x)
def simulated_annealing(initial_solution, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)
    for _ in range(iterations):
        neighbor_solution = current_solution + random.uniform(-0.5, 0.5)
        neighbor_energy = objective_function(neighbor_solution)
        if neighbor_energy < current_energy or random.uniform(0, 1) < math.exp((current_energy - neighbor_energy) / temperature):
            current_solution = neighbor_solution
            current_energy = neighbor_energy
        temperature *= cooling_rate
    return current_solution, objective_function(current_solution)
initial_solution = random.uniform(-10, 10)
initial_temperature = 1000
cooling_rate = 0.95
iterations = 1000
final_solution, final_energy = simulated_annealing(initial_solution, initial_temperature, cooling_rate, iterations)
print(f"Initial Solution: {initial_solution}")
print(f"Final Solution: {final_solution}")
print(f"Objective Function Value: {final_energy}")
