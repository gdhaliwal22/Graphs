"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # enque starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first index
            vertex = q.dequeue()
            # Check if it's been visited
            if vertex not in visited:
                # If it has not been visited
                # Mark it as visited
                print(vertex)
                visited.add(vertex)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty queue or stack as appropriate
        stack = Stack()
        # enque starting vertex_id to the queue
        stack.push(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty:
        while stack.size() > 0:
            # Dequeue the first index
            vertex = stack.pop()
            # Check if it's been visited
            # If it has been visited
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                print(vertex)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None, path=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        s = Stack()  # neighbors to pop off and check if in visited
        s.push(starting_vertex)
        # Check if the node is visited
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Print
                print(v)
                # Call DFT_Recursive on each child
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add a [path to] the starting vertex_id in the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH ([0])
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            vertex = path[-1]
            # CHECK IF IT'S THE TARGET
            if vertex == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # If the vertex has not been visited...
            elif vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()
        # Add a [path to] the starting vertex in stack
        s.push([starting_vertex])
        # Create an empty set to store visited
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first path
            path = s.pop()
            # Grab the last vertex from the path
            vertex = path[-1]
            # Check if it's the target
            if vertex == destination_vertex:
                # If so, return the path
                return path
            # If the vertex hasn't been visited...
            elif vertex not in visited:
                # Add the vertex to visited
                visited.add(vertex)
                # Then add a path to all neighbors
                for neighbor in self.vertices[vertex]:
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # If no vertices have been visited yet...
        if visited is None:
            # Assign an empty set to visited
            visited = set()
        # If no path has been explored...
        if path is None:
            # Assign an empty array to path
            path = []
        # Add the starting vertex to visited
        visited.add(starting_vertex)
        # Reassign path to include the addition of the [visited vertex]
        path = path + [starting_vertex]
        # If we've arrived to the destination vertex (equal to current)...
        if starting_vertex == destination_vertex:
            # Return the path because work is done
            return path
        # For each neighbor found in the get_neighbors method (connected to current vertex)...
        for neighbor in self.get_neighbors(starting_vertex):
            # If the neighbor hasn't been visited yet...
            if neighbor not in visited:
                # Recursively call this function with the neighbor replacing current vertex and assign to new path
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                # If there is a new path...
                if new_path:
                    # Return said path and repeat the above logic until we locate the path to destination
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
