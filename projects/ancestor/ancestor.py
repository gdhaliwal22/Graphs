class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    queue = Queue()
    # Add a [path to] the starting_node in the queue
    queue.enqueue([starting_node])
    # Create a variable for path length and set to 1 (to be used in conditionals)
    path_length = 1
    # Create a variable for earliest ancestor and set to -1 (ditto ^ changing variable)
    earliest_ancestor = -1
    # While the queue is not empty...
    while queue.size() > 0:
        # Dequeue the queue and assign to path
        path = queue.dequeue()
        # Assign the path's last vertex [-1] to farthest
        farthest = path[-1]
        if (len(path) >= path_length and farthest < earliest_ancestor) or len(path) > path_length:
            # Reassign farthest to the earliest_ancestor
            earliest_ancestor = farthest
            # Reassign length of path to path_length
            path_length = len(path)
        for descendant in graph.vertices[farthest]:
            new_path = list(path)
            new_path.append(descendant)
            queue.enqueue(new_path)
    return earliest_ancestor
