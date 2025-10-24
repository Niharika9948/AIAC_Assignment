class Graph:
    def __init__(self):
        # Each key in the adjacency_list dict is a vertex,
        # and the value is a list of neighbors (edges)
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add vertex if it doesn't exist
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v):
        """
        Add an undirected edge between vertex u and vertex v.
        For a directed graph, only append v to u's list.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # Remove this line for directed

    def bfs(self, start):
        """
        Breadth-First Search (BFS) traverses the graph level by level,
        exploring all neighbors before going deeper.
        """
        visited = set()        # To track visited nodes
        queue = []             # Use a list as a queue for simplicity
        traversal_order = []   # Stores the order of traversal

        queue.append(start)
        visited.add(start)

        while queue:
            current = queue.pop(0)  # Dequeue node
            traversal_order.append(current)
            # Visit all neighbors
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    # Enqueue unvisited neighbor

        return traversal_order

    def dfs_recursive(self, start):
        """
        Depth-First Search (DFS) recursive implementation.
        Visits as deep as possible along each branch before backtracking.
        """
        visited = set()
        traversal_order = []

        def dfs(node):
            visited.add(node)
            traversal_order.append(node)
            # Visit all unvisited neighbors recursively
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return traversal_order

    def dfs_iterative(self, start):
        """
        Depth-First Search (DFS) iterative implementation using a stack.
        Useful for avoiding recursion stack overflow on big graphs.
        """
        visited = set()
        stack = [start]
        traversal_order = []

        while stack:
            node = stack.pop()  # Pop last element (LIFO)
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                # Push neighbors to stack. Reverse for consistent order with recursion
                for neighbor in reversed(self.adjacency_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return traversal_order

if __name__ == "__main__":
    # Example graph:
    #   A
    #  / \
    # B   C
    # |   |
    # D---E
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')

    print("Adjacency List:")
    for vertex in g.adjacency_list:
        print(f"{vertex}: {g.adjacency_list[vertex]}")

    print("\nBFS traversal from 'A':")
    print(g.bfs('A'))

    print("\nDFS (recursive) traversal from 'A':")
    print(g.dfs_recursive('A'))

    print("\nDFS (iterative) traversal from 'A':")
    print(g.dfs_iterative('A'))

    # AI Suggestion on DFS:
    # The recursive DFS is shorter and idiomatic for Python, but may hit
    # recursion limits on large/deep graphs. Iterative DFS using a stack
    # avoids this and gives you more control; both yield similar results
    # on connected graphs, but iterative may be preferred for very big graphs.
