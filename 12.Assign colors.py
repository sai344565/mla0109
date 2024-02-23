class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def color_graph(self):
        colors = {}
        for node in self.graph:
            available_colors = set(range(1, len(self.graph) + 1))

            for neighbor in self.graph[node]:
                if neighbor in colors:
                    available_colors.discard(colors[neighbor])

            if available_colors:
                chosen_color = min(available_colors)
                colors[node] = chosen_color
            else:
                raise ValueError("Cannot color the graph with distinct colors.")

        return colors

map_graph = Graph()

map_graph.add_edge("A", "B")
map_graph.add_edge("B", "C")
map_graph.add_edge("C", "D")
map_graph.add_edge("D", "A")
map_graph.add_edge("A", "C")

colors = map_graph.color_graph()

print("Node Colors:")
for node, color in colors.items():
    print(f"{node}: Color {color}")
