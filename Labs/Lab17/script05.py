from math import inf, sqrt
import math
from heapq import heappop, heappush
from euclidean_graph import euclidean_graph, bengaluru, jaipur

# Paste the heuristic() function developed in Step 4 here:
def heuristic(start, target):
    x_distance = abs(target.x - start.x)
    y_distance = abs(target.y - start.y)

    return math.sqrt(x_distance ** 2 + y_distance ** 2)

# Paste the a_star() function developed in Step 4 here:
def a_star(graph, start, target):
    print("Starting A* algorithm!")
    # Paste the a_star() function developed in Step 2 here, and increment count when a change to the path is recorded.
    count = 0
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight
            new_path = paths_and_distances[current_vertex][1] + [neighbor]

        if new_distance < paths_and_distances[neighbor][0]:
            paths_and_distances[neighbor][0] = new_distance
            paths_and_distances[neighbor][1] = new_path

            heappush(vertices_to_explore, (new_distance, neighbor))

            count += 1
            print("\nAt " + vertices_to_explore[0][1].name)

    print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])

    return paths_and_distances[target][1]
# Call a_star() on euclidean_graph to find the best route
# from jaipur to bengaluru:
a_star(euclidean_graph, jaipur, bengaluru)
