class Graph:
    """Graph implementation with both adjacency list and matrix representations"""

    def __init__(self,is_directed=False):
        self.vertices = set()
        self.edges_count = 0 
        self.adjacency_list = {}
        self.is_directed = is_directed
    def add_vertex(self,vertex):
        """Add a vertex to the graph"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertices.add(vertex)
            print(f"Added vertex: {vertex}")

    def add_edge(self,vertex1,vertex2,weight=1):
        """Add an edge between two vertices"""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.edges_count += 1
            if not self.is_directed:
                self.adjacency_list[vertex2].append(vertex1)
            direction = "directed" if self.is_directed else "undirected"
            print(f"Added {direction} edge: {vertex1} -> {vertex2}")
    
    def get_neighbours(self,vertex):
        """Get all neighbors of a vertex"""
        return self.adjacency_list.get(vertex,[])
    
    def display_graph(self):
        """Display the graph structure"""
        print("\n=== Graph Structure ===")
        print(f"Vertices: {sorted(list(self.vertices))}")
        print(f"Total vertices: {len(self.vertices)}")
        print(f"Total edges: {self.edges_count}")
        print(f"Type: {'Directed' if self.is_directed else 'Undirected'}")
        print(f"\nAdjaacency List: ")
        for vertex in sorted(self.adjacency_list.keys()):
            neighbours = self.adjacency_list[vertex]
            print(f"    {vertex}:{neighbours}")
        print("=" * 25)

if __name__ == "__main__":
    print("=" * 60)
    print("GRAPH TRAVERSAL ALGORITHMS - BFS & DFS")
    print("=" * 60)
    
    # Create test graph
    print("\n1. Creating Test Graph...")
    g = Graph(is_directed=False)
    
    # Add edges to create connected graph
    edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"),
        ("C", "F"), ("D", "G"), ("E", "G"), ("F", "G")
    ]
    
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    g.display_graph()
    
    # Initialize traversal
    # traversal = GraphTraversal(g)
    
    # Test BFS
    print("\n2. BFS Traversal Tests:")
    # bfs_result = traversal.bfs("A")
    
    # Test BFS shortest path
    # path, distance = traversal.bfs_shortest_path("A", "G")
    # print(f"\nShortest path A -> G: {path} (distance: {distance})")
    
    # # Test BFS level order
    # traversal.bfs_level_order("A")
    
    # Test DFS
    # print("\n3. DFS Traversal Tests:")
    # dfs_recursive_result = traversal.dfs_recursive("A")
    # print(f"DFS Recursive result: {dfs_recursive_result}")
    
    # dfs_iterative_result = traversal.dfs_iterative("A")
    
    # # Test DFS path finding
    # dfs_path = traversal.dfs_find_path("A", "G")
    # print(f"DFS path A -> G: {dfs_path}")
    
    # # Test cycle detection
    # print(f"\n4. Graph Properties:")
    # has_cycle = traversal.dfs_detect_cycle()
    # print(f"Has cycle: {has_cycle}")
    
    # components = traversal.dfs_connected_components()
    # print(f"Connected components: {components}")
    
    # Test on directed graph
    # print("\n5. Directed Graph Test:")
    # directed_g = Graph(is_directed=True)
    # directed_edges = [("X", "Y"), ("Y", "Z"), ("Z", "X"), ("A", "B")]
    
    # for v1, v2 in directed_edges:
    #     directed_g.add_edge(v1, v2)
    
    # directed_g.display_graph()
    # directed_traversal = GraphTraversal(directed_g)
    # directed_traversal.bfs("X")
    # directed_traversal.dfs_iterative("X")
    
    # Real-world applications
    print("\n6. Real-World Applications:")
    # GraphApplications.social_network_analysis()
    # GraphApplications.maze_solver()
    # GraphApplications.web_crawler()
    
    print("\n" + "="*60)
    print("BFS vs DFS SUMMARY FOR GATE:")
    print("="*60)
    print("BFS (Breadth-First Search):")
    print("  - Uses: QUEUE (FIFO)")
    print("  - Pattern: Level by level")
    print("  - Best for: Shortest path, minimum steps")
    print("  - Time: O(V + E), Space: O(V)")
    print()
    print("DFS (Depth-First Search):")
    print("  - Uses: STACK (LIFO) or Recursion")
    print("  - Pattern: Go deep, then backtrack")  
    print("  - Best for: Any path, cycle detection, topological sort")
    print("  - Time: O(V + E), Space: O(V)")
    print()
    print("Memory Trick:")
    print("  - BFS = 'Be Fair to neighbors' (visit all neighbors first)")
    print("  - DFS = 'Dive Deep First' (go as deep as possible)")
    print("="*60)
