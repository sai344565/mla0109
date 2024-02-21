import sys
def nearest_neighbor(graph):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = [0]  
    for _ in range(num_cities - 1):
        current_city = tour[-1]
        nearest_city = find_nearest_neighbor(graph, current_city, visited)
        tour.append(nearest_city)
        visited[nearest_city] = True
    tour.append(tour[0])
    return tour
def find_nearest_neighbor(graph, current_city, visited):
    min_distance = sys.maxsize
    nearest_city = -1
    for city, distance in enumerate(graph[current_city]):
        if not visited[city] and distance < min_distance:
            min_distance = distance
            nearest_city = city
    return nearest_city
cities = ["City A", "City B", "City C", "City D"]
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
tour = nearest_neighbor(graph)
print("Optimal Tour:", [cities[i] for i in tour])
