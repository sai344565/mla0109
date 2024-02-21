def water_jug_problem(capacity_4gallon, capacity_3gallon, target):
    jug_4gallon = 0
    jug_3gallon = 0
    while jug_4gallon != target:
        jug_4gallon = capacity_4gallon if jug_4gallon + capacity_4gallon <= capacity_4gallon else jug_4gallon + capacity_4gallon
        pour_amount = min(jug_4gallon, capacity_3gallon - jug_3gallon)
        jug_4gallon -= pour_amount
        jug_3gallon += pour_amount
        jug_3gallon = 0
        if jug_4gallon == target:
            break
    return jug_4gallon, jug_3gallon
capacity_4gallon = 4
capacity_3gallon = 3
target = 2
result = water_jug_problem(capacity_4gallon, capacity_3gallon, target)
if result[0] == target:
    print(f"Successfully obtained {target} gallons in the 4-gallon jug.")
    print(f"Final state: 4-gallon jug = {result[0]}, 3-gallon jug = {result[1]}")
else:
    print("It's not possible to obtain exactly 2 gallons in the 4-gallon jug.")
