from collections import deque

class Graph:
    """Graph implementation with both adjacency list and matrix representations"""
    
    def __init__(self, is_directed=False):
        self.adjacency_list = {}  # Dictionary representation
        self.is_directed = is_directed
        self.vertices = set()
        self.edge_count = 0
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertices.add(vertex)
            print(f"Added vertex: {vertex}")
    
    def add_edge(self, vertex1, vertex2, weight=1):
        """Add an edge between two vertices"""
        # Add vertices if they don't exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        # Add edge
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.edge_count += 1
            
            # If undirected, add reverse edge
            if not self.is_directed:
                self.adjacency_list[vertex2].append(vertex1)
            
            direction = "directed" if self.is_directed else "undirected"
            print(f"Added {direction} edge: {vertex1} -> {vertex2}")
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        return self.adjacency_list.get(vertex, [])
    
    def display_graph(self):
        """Display the graph structure"""
        print("\n=== Graph Structure ===")
        print(f"Vertices: {sorted(list(self.vertices))}")
        print(f"Total vertices: {len(self.vertices)}")
        print(f"Total edges: {self.edge_count}")
        print(f"Type: {'Directed' if self.is_directed else 'Undirected'}")
        
        print("\nAdjacency List:")
        for vertex in sorted(self.adjacency_list.keys()):
            neighbors = self.adjacency_list[vertex]
            print(f"  {vertex}: {neighbors}")
        print("=" * 25)

class GraphTraversal:
    """Graph traversal algorithms - BFS and DFS implementations"""
    
    def __init__(self, graph):
        self.graph = graph
    
    # ============ BREADTH-FIRST SEARCH (BFS) ============
    
    def bfs(self, start_vertex):
        """
        BFS Traversal - Level by level exploration
        Uses QUEUE (First In, First Out)
        Great for: Shortest path, minimum steps problems
        Time: O(V + E), Space: O(V)
        """
        if start_vertex not in self.graph.vertices:
            print(f"Vertex {start_vertex} not found in graph!")
            return []
        
        visited = set()
        queue = deque([start_vertex])
        traversal_order = []
        
        print(f"\n=== BFS Traversal starting from {start_vertex} ===")
        
        while queue:
            # Dequeue front element (FIFO - First In, First Out)
            current_vertex = queue.popleft()
            
            if current_vertex not in visited:
                # Mark as visited and add to result
                visited.add(current_vertex)
                traversal_order.append(current_vertex)
                print(f"Visited: {current_vertex}")
                
                # Add all unvisited neighbors to queue
                neighbors = self.graph.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        print(f"  Added to queue: {neighbor}")
                
                print(f"  Current queue: {list(queue)}")
        
        print(f"BFS Complete! Order: {traversal_order}")
        return traversal_order
    
    def bfs_shortest_path(self, start, target):
        """
        Find shortest path between two vertices using BFS
        Returns path and distance
        """
        if start not in self.graph.vertices or target not in self.graph.vertices:
            return None, -1
        
        if start == target:
            return [start], 0
        
        visited = set()
        queue = deque([(start, [start])])  # (vertex, path_to_vertex)
        
        print(f"\n=== BFS Shortest Path: {start} -> {target} ===")
        
        while queue:
            current_vertex, path = queue.popleft()
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            print(f"Exploring: {current_vertex}, Current path: {path}")
            
            # Check all neighbors
            for neighbor in self.graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    
                    # Found target!
                    if neighbor == target:
                        print(f"Found target! Path: {new_path}")
                        return new_path, len(new_path) - 1
                    
                    queue.append((neighbor, new_path))
        
        print("No path found!")
        return None, -1
    
    def bfs_level_order(self, start_vertex):
        """
        BFS that returns nodes grouped by levels/distance from start
        """
        if start_vertex not in self.graph.vertices:
            return []
        
        visited = set()
        queue = deque([(start_vertex, 0)])  # (vertex, level)
        levels = {}
        
        print(f"\n=== BFS Level Order from {start_vertex} ===")
        
        while queue:
            current_vertex, level = queue.popleft()
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            # Add to appropriate level
            if level not in levels:
                levels[level] = []
            levels[level].append(current_vertex)
            
            # Add neighbors to next level
            for neighbor in self.graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
        
        # Display results
        for level in sorted(levels.keys()):
            print(f"Level {level}: {levels[level]}")
        
        return levels
    
    # ============ DEPTH-FIRST SEARCH (DFS) ============
    
    def dfs_recursive(self, start_vertex, visited=None):
        """
        DFS Traversal - Recursive implementation
        Goes as deep as possible down one path
        Time: O(V + E), Space: O(V)
        """
        if visited is None:
            visited = set()
            print(f"\n=== DFS Recursive starting from {start_vertex} ===")
        
        if start_vertex not in self.graph.vertices:
            print(f"Vertex {start_vertex} not found in graph!")
            return []
        
        # Mark current vertex as visited
        visited.add(start_vertex)
        traversal_order = [start_vertex]
        print(f"Visited: {start_vertex}")
        
        # Recursively visit all unvisited neighbors
        neighbors = self.graph.get_neighbors(start_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                print(f"  Going deeper to: {neighbor}")
                traversal_order.extend(self.dfs_recursive(neighbor, visited))
        
        return traversal_order
    
    def dfs_iterative(self, start_vertex):
        """
        DFS Traversal - Iterative implementation using stack
        Uses STACK (Last In, First Out)
        Great for: Pathfinding, cycle detection, topological sort
        """
        if start_vertex not in self.graph.vertices:
            print(f"Vertex {start_vertex} not found in graph!")
            return []
        
        visited = set()
        stack = [start_vertex]
        traversal_order = []
        
        print(f"\n=== DFS Iterative starting from {start_vertex} ===")
        
        while stack:
            # Pop from top of stack (LIFO - Last In, First Out)
            current_vertex = stack.pop()
            
            if current_vertex not in visited:
                # Mark as visited and add to result
                visited.add(current_vertex)
                traversal_order.append(current_vertex)
                print(f"Visited: {current_vertex}")
                
                # Add all unvisited neighbors to stack
                # Add in reverse order to maintain left-to-right traversal
                neighbors = self.graph.get_neighbors(current_vertex)
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        print(f"  Added to stack: {neighbor}")
                
                print(f"  Current stack: {stack}")
        
        print(f"DFS Complete! Order: {traversal_order}")
        return traversal_order
    
    def dfs_find_path(self, start, target):
        """
        Find ANY path between two vertices using DFS
        Returns first path found (not necessarily shortest)
        """
        if start not in self.graph.vertices or target not in self.graph.vertices:
            return None
        
        visited = set()
        stack = [(start, [start])]  # (vertex, path_to_vertex)
        
        print(f"\n=== DFS Path Finding: {start} -> {target} ===")
        
        while stack:
            current_vertex, path = stack.pop()
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            print(f"Exploring: {current_vertex}, Current path: {path}")
            
            # Found target!
            if current_vertex == target:
                print(f"Found target! Path: {path}")
                return path
            
            # Add neighbors to stack
            for neighbor in self.graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))
        
        print("No path found!")
        return None
    
    def dfs_detect_cycle(self):
        """
        Detect cycle in graph using DFS
        For undirected graphs
        """
        visited = set()
        
        def has_cycle(vertex, parent):
            visited.add(vertex)
            
            for neighbor in self.graph.get_neighbors(vertex):
                if neighbor not in visited:
                    if has_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:  # Back edge found
                    return True
            
            return False
        
        # Check all components
        for vertex in self.graph.vertices:
            if vertex not in visited:
                if has_cycle(vertex, None):
                    return True
        
        return False
    
    def dfs_connected_components(self):
        """
        Find all connected components using DFS
        """
        visited = set()
        components = []
        
        def dfs_component(vertex, component):
            visited.add(vertex)
            component.append(vertex)
            
            for neighbor in self.graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_component(neighbor, component)
        
        for vertex in self.graph.vertices:
            if vertex not in visited:
                component = []
                dfs_component(vertex, component)
                components.append(component)
        
        return components

# ============ APPLICATION EXAMPLES ============

class GraphApplications:
    """Real-world applications of BFS and DFS"""
    
    @staticmethod
    def social_network_analysis():
        """Example: Social network friend recommendations"""
        print("\n" + "="*50)
        print("SOCIAL NETWORK EXAMPLE")
        print("="*50)
        
        # Create social network
        social_graph = Graph(is_directed=False)
        
        # Add friendships
        friendships = [
            ("Alice", "Bob"), ("Alice", "Charlie"), 
            ("Bob", "David"), ("Charlie", "Eve"),
            ("David", "Frank"), ("Eve", "Frank"),
            ("Grace", "Henry")  # Separate component
        ]
        
        for person1, person2 in friendships:
            social_graph.add_edge(person1, person2)
        
        social_graph.display_graph()
        
        traversal = GraphTraversal(social_graph)
        
        # Find shortest path (degrees of separation)
        path, distance = traversal.bfs_shortest_path("Alice", "Frank")
        if path:
            print(f"\nDegrees of separation (Alice -> Frank): {distance}")
            print(f"Connection path: {' -> '.join(path)}")
        
        # Find connected components (friend groups)
        components = traversal.dfs_connected_components()
        print(f"\nFriend groups: {components}")
    
    @staticmethod  
    def maze_solver():
        """Example: Maze solving using DFS"""
        print("\n" + "="*50)
        print("MAZE SOLVING EXAMPLE")
        print("="*50)
        
        # Create maze as graph
        maze = Graph(is_directed=False)
        
        # Maze connections (simplified)
        maze_paths = [
            ("Start", "A"), ("A", "B"), ("A", "C"),
            ("B", "Dead_End"), ("C", "D"), ("C", "E"),
            ("D", "End"), ("E", "F"), ("F", "End")
        ]
        
        for path1, path2 in maze_paths:
            maze.add_edge(path1, path2)
        
        maze.display_graph()
        
        traversal = GraphTraversal(maze)
        
        # Find path through maze
        path = traversal.dfs_find_path("Start", "End")
        if path:
            print(f"\nMaze solution path: {' -> '.join(path)}")
    
    @staticmethod
    def web_crawler():
        """Example: Web crawling using BFS"""
        print("\n" + "="*50)
        print("WEB CRAWLER EXAMPLE")
        print("="*50)
        
        # Create web graph
        web = Graph(is_directed=True)
        
        # Web page links
        web_links = [
            ("HomePage", "About"), ("HomePage", "Products"),
            ("About", "Contact"), ("Products", "Product1"),
            ("Products", "Product2"), ("Product1", "Reviews"),
            ("Product2", "Reviews"), ("Contact", "HomePage")
        ]
        
        for page1, page2 in web_links:
            web.add_edge(page1, page2)
        
        web.display_graph()
        
        traversal = GraphTraversal(web)
        
        # Crawl web pages level by level
        levels = traversal.bfs_level_order("HomePage")
        print("\nWeb crawl results (by distance from homepage):")

# ============ COMPREHENSIVE TESTING ============

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
    traversal = GraphTraversal(g)
    
    # Test BFS
    print("\n2. BFS Traversal Tests:")
    bfs_result = traversal.bfs("A")
    
    # Test BFS shortest path
    path, distance = traversal.bfs_shortest_path("A", "G")
    print(f"\nShortest path A -> G: {path} (distance: {distance})")
    
    # Test BFS level order
    traversal.bfs_level_order("A")
    
    # Test DFS
    print("\n3. DFS Traversal Tests:")
    dfs_recursive_result = traversal.dfs_recursive("A")
    print(f"DFS Recursive result: {dfs_recursive_result}")
    
    dfs_iterative_result = traversal.dfs_iterative("A")
    
    # Test DFS path finding
    dfs_path = traversal.dfs_find_path("A", "G")
    print(f"DFS path A -> G: {dfs_path}")
    
    # Test cycle detection
    print(f"\n4. Graph Properties:")
    has_cycle = traversal.dfs_detect_cycle()
    print(f"Has cycle: {has_cycle}")
    
    components = traversal.dfs_connected_components()
    print(f"Connected components: {components}")
    
    # Test on directed graph
    print("\n5. Directed Graph Test:")
    directed_g = Graph(is_directed=True)
    directed_edges = [("X", "Y"), ("Y", "Z"), ("Z", "X"), ("A", "B")]
    
    for v1, v2 in directed_edges:
        directed_g.add_edge(v1, v2)
    
    directed_g.display_graph()
    directed_traversal = GraphTraversal(directed_g)
    directed_traversal.bfs("X")
    directed_traversal.dfs_iterative("X")
    
    # Real-world applications
    print("\n6. Real-World Applications:")
    GraphApplications.social_network_analysis()
    GraphApplications.maze_solver()
    GraphApplications.web_crawler()
    
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

    import heapq
import math
from collections import defaultdict

class WeightedGraph:
    """Weighted graph implementation for pathfinding algorithms"""
    
    def __init__(self, is_directed=False):
        self.adjacency_list = defaultdict(list)  # vertex -> [(neighbor, weight), ...]
        self.vertices = set()
        self.is_directed = is_directed
        self.edge_count = 0
        
        # For grid-based pathfinding (A*)
        self.coordinates = {}  # vertex -> (x, y) for heuristic calculations
    
    def add_vertex(self, vertex, x=None, y=None):
        """Add vertex with optional coordinates for A* heuristic"""
        self.vertices.add(vertex)
        if x is not None and y is not None:
            self.coordinates[vertex] = (x, y)
        print(f"Added vertex: {vertex}" + (f" at ({x}, {y})" if x is not None else ""))
    
    def add_edge(self, vertex1, vertex2, weight):
        """Add weighted edge between vertices"""
        # Add vertices if they don't exist
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        
        # Add edge
        self.adjacency_list[vertex1].append((vertex2, weight))
        self.edge_count += 1
        
        # If undirected, add reverse edge
        if not self.is_directed:
            self.adjacency_list[vertex2].append((vertex1, weight))
        
        direction = "directed" if self.is_directed else "undirected"
        print(f"Added {direction} edge: {vertex1} -> {vertex2} (weight: {weight})")
    
    def get_neighbors(self, vertex):
        """Get neighbors with weights: [(neighbor, weight), ...]"""
        return self.adjacency_list[vertex]
    
    def display_graph(self):
        """Display graph structure"""
        print(f"\n{'='*30}")
        print("WEIGHTED GRAPH STRUCTURE")
        print(f"{'='*30}")
        print(f"Vertices: {sorted(list(self.vertices))}")
        print(f"Edges: {self.edge_count}")
        print(f"Type: {'Directed' if self.is_directed else 'Undirected'}")
        
        print("\nAdjacency List (with weights):")
        for vertex in sorted(self.adjacency_list.keys()):
            neighbors = self.adjacency_list[vertex]
            print(f"  {vertex}: {neighbors}")
        print(f"{'='*30}")

class DijkstraAlgorithm:
    """Dijkstra's Algorithm - Shortest path to ALL vertices"""
    
    def __init__(self, graph):
        self.graph = graph
    
    def find_shortest_paths(self, start_vertex):
        """
        Dijkstra's Algorithm Implementation
        Returns: (distances, previous_vertices) dictionaries
        
        Time Complexity: O((V + E) log V) with priority queue
        Space Complexity: O(V)
        """
        if start_vertex not in self.graph.vertices:
            print(f"Start vertex {start_vertex} not found!")
            return {}, {}
        
        # Initialize distances and previous vertices
        distances = {vertex: float('inf') for vertex in self.graph.vertices}
        previous = {vertex: None for vertex in self.graph.vertices}
        distances[start_vertex] = 0
        
        # Priority queue: [(distance, vertex), ...]
        priority_queue = [(0, start_vertex)]
        visited = set()
        
        print(f"\n{'='*50}")
        print(f"DIJKSTRA'S ALGORITHM FROM {start_vertex}")
        print(f"{'='*50}")
        print(f"Initial distances: {distances}")
        
        step = 1
        while priority_queue:
            # Get vertex with minimum distance (greedy choice)
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Skip if already processed (duplicate in priority queue)
            if current_vertex in visited:
                continue
            
            # Mark as visited
            visited.add(current_vertex)
            
            print(f"\nStep {step}: Processing vertex '{current_vertex}' (distance: {current_distance})")
            
            # Check all neighbors
            for neighbor, weight in self.graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    # Calculate new distance through current vertex
                    new_distance = distances[current_vertex] + weight
                    
                    # If we found a shorter path, update it
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_vertex
                        heapq.heappush(priority_queue, (new_distance, neighbor))
                        
                        print(f"  Updated {neighbor}: distance = {new_distance} (via {current_vertex})")
                    else:
                        print(f"  {neighbor}: no improvement (current: {distances[neighbor]}, new: {new_distance})")
            
            print(f"  Current distances: {distances}")
            print(f"  Visited: {sorted(list(visited))}")
            print(f"  Queue: {sorted(priority_queue)}")
            step += 1
        
        print(f"\n{'='*30}")
        print("DIJKSTRA'S RESULTS:")
        print(f"{'='*30}")
        for vertex in sorted(distances.keys()):
            if distances[vertex] == float('inf'):
                print(f"{start_vertex} -> {vertex}: No path")
            else:
                path = self._reconstruct_path(previous, start_vertex, vertex)
                print(f"{start_vertex} -> {vertex}: distance = {distances[vertex]}, path = {' -> '.join(path)}")
        
        return distances, previous
    
    def _reconstruct_path(self, previous, start, target):
        """Reconstruct path from start to target using previous vertices"""
        path = []
        current = target
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        
        # Check if path is valid
        if path[0] != start:
            return []  # No path exists
        
        return path
    
    def shortest_path(self, start, target):
        """Find shortest path between two specific vertices"""
        distances, previous = self.find_shortest_paths(start)
        
        if distances[target] == float('inf'):
            return None, float('inf')
        
        path = self._reconstruct_path(previous, start, target)
        return path, distances[target]

class AStarAlgorithm:
    """A* Algorithm - Heuristic-based pathfinding to specific target"""
    
    def __init__(self, graph):
        self.graph = graph
    
    def manhattan_distance(self, vertex1, vertex2):
        """Manhattan distance heuristic (|x1-x2| + |y1-y2|)"""
        if vertex1 not in self.graph.coordinates or vertex2 not in self.graph.coordinates:
            return 0  # No heuristic available
        
        x1, y1 = self.graph.coordinates[vertex1]
        x2, y2 = self.graph.coordinates[vertex2]
        return abs(x1 - x2) + abs(y1 - y2)
    
    def euclidean_distance(self, vertex1, vertex2):
        """Euclidean distance heuristic (straight line distance)"""
        if vertex1 not in self.graph.coordinates or vertex2 not in self.graph.coordinates:
            return 0  # No heuristic available
        
        x1, y1 = self.graph.coordinates[vertex1]
        x2, y2 = self.graph.coordinates[vertex2]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    def find_path(self, start, target, heuristic='manhattan'):
        """
        A* Algorithm Implementation
        
        f(n) = g(n) + h(n) where:
        - g(n) = actual cost from start to n
        - h(n) = heuristic estimate from n to target
        - f(n) = total estimated cost
        
        Time Complexity: O(b^d) where b=branching factor, d=depth
        Space Complexity: O(b^d)
        """
        if start not in self.graph.vertices or target not in self.graph.vertices:
            print(f"Start or target vertex not found!")
            return None, float('inf')
        
        if start == target:
            return [start], 0
        
        # Choose heuristic function
        if heuristic == 'euclidean':
            h_func = self.euclidean_distance
        else:
            h_func = self.manhattan_distance
        
        # Initialize data structures
        open_set = []  # Priority queue: [(f_score, vertex), ...]
        closed_set = set()  # Visited vertices
        
        g_score = {vertex: float('inf') for vertex in self.graph.vertices}
        g_score[start] = 0
        
        f_score = {vertex: float('inf') for vertex in self.graph.vertices}
        f_score[start] = h_func(start, target)
        
        previous = {vertex: None for vertex in self.graph.vertices}
        
        heapq.heappush(open_set, (f_score[start], start))
        
        print(f"\n{'='*60}")
        print(f"A* ALGORITHM: {start} -> {target} (heuristic: {heuristic})")
        print(f"{'='*60}")
        print(f"Target coordinates: {self.graph.coordinates.get(target, 'N/A')}")
        
        step = 1
        while open_set:
            # Get vertex with lowest f_score
            current_f, current = heapq.heappop(open_set)
            
            # Skip if already processed
            if current in closed_set:
                continue
            
            # Add to closed set
            closed_set.add(current)
            
            print(f"\nStep {step}: Exploring '{current}'")
            print(f"  g(n) = {g_score[current]:.2f}, h(n) = {h_func(current, target):.2f}, f(n) = {current_f:.2f}")
            
            # Found target!
            if current == target:
                path = self._reconstruct_path(previous, start, target)
                total_cost = g_score[target]
                
                print(f"\n🎯 TARGET FOUND!")
                print(f"Path: {' -> '.join(path)}")
                print(f"Total cost: {total_cost}")
                print(f"Steps explored: {step}")
                
                return path, total_cost
            
            # Explore neighbors
            for neighbor, weight in self.graph.get_neighbors(current):
                if neighbor in closed_set:
                    continue
                
                # Calculate tentative g_score
                tentative_g = g_score[current] + weight
                
                # If this path is better
                if tentative_g < g_score[neighbor]:
                    # Update path
                    previous[neighbor] = current
                    g_score[neighbor] = tentative_g
                    h_value = h_func(neighbor, target)
                    f_score[neighbor] = tentative_g + h_value
                    
                    # Add to open set
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    
                    print(f"    Added/Updated {neighbor}: g={tentative_g:.2f}, h={h_value:.2f}, f={f_score[neighbor]:.2f}")
            
            step += 1
        
        print(f"\n❌ No path found from {start} to {target}")
        return None, float('inf')
    
    def _reconstruct_path(self, previous, start, target):
        """Reconstruct path from previous vertices dictionary"""
        path = []
        current = target
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        return path

class PathfindingComparison:
    """Compare Dijkstra's vs A* performance and results"""
    
    @staticmethod
    def compare_algorithms(graph, start, target):
        """Compare Dijkstra's and A* on the same problem"""
        print(f"\n{'='*70}")
        print(f"ALGORITHM COMPARISON: {start} -> {target}")
        print(f"{'='*70}")
        
        # Run Dijkstra's
        dijkstra = DijkstraAlgorithm(graph)
        dijkstra_path, dijkstra_cost = dijkstra.shortest_path(start, target)
        
        # Run A* with Manhattan heuristic
        astar = AStarAlgorithm(graph)
        astar_path_manhattan, astar_cost_manhattan = astar.find_path(start, target, 'manhattan')
        
        # Run A* with Euclidean heuristic  
        astar_path_euclidean, astar_cost_euclidean = astar.find_path(start, target, 'euclidean')
        
        # Compare results
        print(f"\n{'='*40}")
        print("COMPARISON RESULTS:")
        print(f"{'='*40}")
        print(f"Dijkstra's:")
        print(f"  Path: {' -> '.join(dijkstra_path) if dijkstra_path else 'No path'}")
        print(f"  Cost: {dijkstra_cost}")
        
        print(f"\nA* (Manhattan):")
        print(f"  Path: {' -> '.join(astar_path_manhattan) if astar_path_manhattan else 'No path'}")
        print(f"  Cost: {astar_cost_manhattan}")
        
        print(f"\nA* (Euclidean):")
        print(f"  Path: {' -> '.join(astar_path_euclidean) if astar_path_euclidean else 'No path'}")
        print(f"  Cost: {astar_cost_euclidean}")
        
        # Verify optimality
        if dijkstra_cost == astar_cost_manhattan == astar_cost_euclidean:
            print(f"\n✅ All algorithms found optimal solution with cost {dijkstra_cost}")
        else:
            print(f"\n⚠️ Different costs found - check heuristic admissibility!")

class GridWorld:
    """Create grid-based world for pathfinding demonstration"""
    
    @staticmethod
    def create_grid_graph(width, height, obstacles=None):
        """Create grid world with optional obstacles"""
        if obstacles is None:
            obstacles = set()
        
        graph = WeightedGraph(is_directed=False)
        
        # Add all grid vertices with coordinates
        for x in range(width):
            for y in range(height):
                if (x, y) not in obstacles:
                    vertex_name = f"({x},{y})"
                    graph.add_vertex(vertex_name, x, y)
        
        # Add edges between adjacent cells (4-connected)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, right, down, left
        
        for x in range(width):
            for y in range(height):
                if (x, y) not in obstacles:
                    current = f"({x},{y})"
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        
                        # Check bounds and obstacles
                        if (0 <= nx < width and 0 <= ny < height and 
                            (nx, ny) not in obstacles):
                            neighbor = f"({nx},{ny})"
                            
                            # Add edge with weight 1 (uniform cost)
                            if neighbor in graph.vertices:
                                # Only add edge once for undirected graph
                                if current < neighbor:  # Lexicographic comparison to avoid duplicates
                                    graph.add_edge(current, neighbor, 1)
        
        return graph

# ============ COMPREHENSIVE EXAMPLES AND TESTING ============

if __name__ == "__main__":
    print("=" * 80)
    print("DIJKSTRA'S ALGORITHM & A* ALGORITHM IMPLEMENTATION")
    print("=" * 80)
    
    # Example 1: Simple weighted graph
    print("\n1. SIMPLE WEIGHTED GRAPH EXAMPLE:")
    print("-" * 40)
    
    graph1 = WeightedGraph(is_directed=False)
    
    # Add vertices with coordinates for A* heuristic
    vertices_coords = [
        ('A', 0, 0), ('B', 1, 2), ('C', 3, 1), 
        ('D', 2, 3), ('E', 4, 2), ('F', 5, 0)
    ]
    
    for vertex, x, y in vertices_coords:
        graph1.add_vertex(vertex, x, y)
    
    # Add weighted edges
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1),
        ('B', 'D', 5), ('C', 'E', 10), ('D', 'E', 3),
        ('E', 'F', 2), ('C', 'F', 8)
    ]
    
    for v1, v2, weight in edges:
        graph1.add_edge(v1, v2, weight)
    
    graph1.display_graph()
    
    # Test Dijkstra's Algorithm
    dijkstra1 = DijkstraAlgorithm(graph1)
    dijkstra1.find_shortest_paths('A')
    
    # Test A* Algorithm
    astar1 = AStarAlgorithm(graph1)
    astar1.find_path('A', 'F', 'manhattan')
    astar1.find_path('A', 'F', 'euclidean')
    
    # Compare algorithms
    PathfindingComparison.compare_algorithms(graph1, 'A', 'F')
    
    # Example 2: Grid World with obstacles
    print("\n\n2. GRID WORLD PATHFINDING EXAMPLE:")
    print("-" * 50)
    
    # Create 6x5 grid with some obstacles
    obstacles = {(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (4, 3)}
    grid_graph = GridWorld.create_grid_graph(6, 5, obstacles)
    
    print(f"Created 6x5 grid with obstacles at: {obstacles}")
    print(f"Grid has {len(grid_graph.vertices)} walkable cells")
    
    start_cell = "(0,0)"  # Bottom-left
    target_cell = "(5,4)"  # Top-right
    
    print(f"\nFinding path from {start_cell} to {target_cell}")
    
    # Test on grid
    grid_dijkstra = DijkstraAlgorithm(grid_graph)
    grid_path, grid_cost = grid_dijkstra.shortest_path(start_cell, target_cell)
    
    grid_astar = AStarAlgorithm(grid_graph)
    astar_grid_path, astar_grid_cost = grid_astar.find_path(start_cell, target_cell, 'manhattan')
    
    PathfindingComparison.compare_algorithms(grid_graph, start_cell, target_cell)
    
    # Example 3: Real-world scenario - City navigation
    print("\n\n3. CITY NAVIGATION EXAMPLE:")
    print("-" * 40)
    
    city_graph = WeightedGraph(is_directed=False)
    
    # Cities with GPS coordinates (simplified)
    cities = [
        ('Home', 0, 0), ('School', 3, 4), ('Mall', 6, 1),
        ('Hospital', 2, 6), ('Office', 8, 3), ('Airport', 10, 8)
    ]
    
    for city, x, y in cities:
        city_graph.add_vertex(city, x, y)
    
    # Roads with distances (in km)
    roads = [
        ('Home', 'School', 5), ('Home', 'Mall', 7), 
        ('School', 'Hospital', 3), ('School', 'Mall', 4),
        ('Mall', 'Office', 3), ('Hospital', 'Office', 6),
        ('Office', 'Airport', 5), ('Hospital', 'Airport', 8)
    ]
    
    for city1, city2, distance in roads:
        city_graph.add_edge(city1, city2, distance)
    
    city_graph.display_graph()
    
    # Navigate from Home to Airport
    PathfindingComparison.compare_algorithms(city_graph, 'Home', 'Airport')
    
    # Summary for GATE preparation
    print("\n" + "="*80)
    print("ALGORITHM SUMMARY FOR GATE EXAM")
    print("="*80)
    print("""
DIJKSTRA'S ALGORITHM:
✅ Purpose: Shortest path from source to ALL vertices
✅ Guarantees: Optimal solution (always finds shortest path)
✅ Time: O((V + E) log V) with priority queue
✅ Space: O(V)
✅ Best for: Single source, multiple targets
✅ Key insight: Greedy - always process closest unvisited vertex

A* ALGORITHM:
⭐ Purpose: Shortest path from source to SPECIFIC target
⭐ Guarantees: Optimal if heuristic is admissible (never overestimates)
⭐ Time: O(b^d) depends on heuristic quality
⭐ Space: O(b^d) 
⭐ Best for: Single source, single target with good heuristic
⭐ Key insight: Guided search using f(n) = g(n) + h(n)

WHEN TO USE WHICH:
🎯 Use Dijkstra's: Need paths to multiple destinations, no good heuristic
🎯 Use A*: Need path to one destination, have domain knowledge for heuristic

HEURISTIC FUNCTIONS:
📏 Manhattan: |x1-x2| + |y1-y2| (4-connected grids)
📏 Euclidean: √[(x1-x2)² + (y1-y2)²] (any direction movement)
📏 Must be admissible (never overestimate) for optimal A*
    """)
    print("="*80)