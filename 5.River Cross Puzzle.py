def is_valid_state(state):
    for side in state:
        missionaries, cannibals = side
        if missionaries < 0 or cannibals < 0 or (cannibals > missionaries > 0):
            return False
    return True
def is_goal_state(state, total_missionaries):
    return state[1] == [total_missionaries, 0]
def generate_next_states(state, moves):
    next_states = []
    for move in moves:
        new_state = [state[0][:], state[1][:]]
        for i in range(2):
            new_state[i] = [new_state[i][0] - move[i], new_state[i][1] + move[i]]
        if is_valid_state(new_state):
            next_states.append(new_state)
    return next_states
def solve(total_missionaries, total_cannibals):
    start_state = [[total_missionaries, total_cannibals], [0, 0]]
    goal_state = [[0, 0], [total_missionaries, total_cannibals]]
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    stack = [(start_state, [])]
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path
        next_states = generate_next_states(current_state, moves)
        for next_state in next_states:
            if next_state not in path:
                stack.append((next_state, path + [next_state]))
    return None
def print_solution(path):
    if path:
        for i, state in enumerate(path):
            print(f"Step {i + 1}: {state}")
    else:
        print("No solution found.")
total_missionaries = 3
total_cannibals = 3
solution_path = solve(total_missionaries, total_cannibals)
print_solution(solution_path)
