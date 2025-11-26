import heapq
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }


# Define dijkstras() below:
def dijkstras(graph, start):
    distance = {}

    for vertex in graph:
        distance[vertex] = inf

    distance[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heapq.heappop(vertices_to_explore)
        for neighbour, edge_weight in graph[current_vertex]:
            new_distance = sum([current_distance, edge_weight])
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
                heapq.heappush(vertices_to_explore, (new_distance, neighbour))
    return distance

distances_from_a = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_a))