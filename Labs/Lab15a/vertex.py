class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        print(f"Adding edge from {self.value} to {vertex} with weight {weight}")
        self.edges[vertex] = weight

station = Vertex("Cronk")
