# Bring in the Vertex class from vertex.py
from vertex import Vertex

# Define Graph below...
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding " + vertex.value)
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        print(f"Adding edge from {from_vertex.value} to {to_vertex.value}")
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        print(f"Searching path from {start_vertex} to {end_vertex}")
        start = [start_vertex]
        while start:
            current_vertex = start.pop(0)
            print(current_vertex)
            if current_vertex == end_vertex:
                return True
            vertex = self.graph_dict.get(current_vertex)
            next_vertice = vertex.get_edges()
            # add the next vertices to the start list
            start.extend(next_vertice)
            print(current_vertex)
        return False

grand_central = Vertex("Grand Central Station")

# Uncomment this code after you've defined Graph
railway = Graph()

# Uncomment these lines after you've completed .add_vertex()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)