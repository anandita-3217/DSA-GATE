# Graph Theory for GATE DA 2026 🚀
*A friendly, ADHD-brain approved guide with Python code!*

## 🎯 Quick Navigation (Jump anywhere!)
- [What ARE Graphs?](#what-are-graphs)
- [Basic Vocabulary](#basic-vocabulary) 
- [Types of Graphs](#types-of-graphs)
- [Graph Representations](#graph-representations)
- [Traversal Algorithms](#traversal-algorithms)
- [Shortest Path Algorithms](#shortest-path-algorithms)
- [Python Cheat Sheet](#python-cheat-sheet)
- [GATE Exam Tips](#gate-exam-tips)

---

## What ARE Graphs? 🤔

**Think of it like this:** Remember those "Six Degrees of Kevin Bacon" games? Or how Facebook shows "mutual friends"? That's a graph!

**Formal definition:** A graph G = (V, E) where:
- V = Vertices (nodes/points) - like people in your social network
- E = Edges (connections) - like friendships between people

**Real world examples:**
- 🌐 Web pages (vertices) connected by links (edges)
- 🚌 Bus stops (vertices) connected by routes (edges)  
- 🧬 Molecules (vertices) connected by bonds (edges)

---

## Basic Vocabulary 📚

### Core Terms (Learn these first!)

| Term | Simple Explanation | Example |
|------|-------------------|---------|
| **Vertex/Node** | A point in the graph | Person in social network |
| **Edge** | Connection between two vertices | Friendship between two people |
| **Degree** | Number of edges connected to a vertex | Number of friends someone has |
| **Path** | Sequence of vertices connected by edges | Route from home to school |
| **Cycle** | Path that starts and ends at same vertex | Circular route |

### Advanced Terms (Once you're comfortable)

| Term | Explanation | 
|------|-------------|
| **Adjacent vertices** | Vertices connected by an edge |
| **Incident edge** | Edge connected to a vertex |
| **Subgraph** | Part of a larger graph |
| **Complete graph** | Every vertex connected to every other vertex |

---

## Types of Graphs 🎨

### 1. Directed vs Undirected

**Undirected Graph** 
- Edges have no direction (like mutual friendships)
- If A connects to B, then B connects to A

**Directed Graph (Digraph)**
- Edges have direction (like following someone on Twitter)
- A can point to B without B pointing back to A

### 2. Weighted vs Unweighted

**Unweighted Graph**
- All connections are equal (simple yes/no friendship)

**Weighted Graph** 
- Edges have values/costs (distance between cities)

### 3. Special Types

- **Tree:** Connected graph with no cycles
- **Forest:** Collection of trees  
- **Complete Graph:** Every vertex connects to every other
- **Bipartite:** Vertices split into two groups, edges only between groups

---

## Graph Representations 💻

### 1. Adjacency Matrix
**What:** 2D array where [i][j] = 1 if edge exists between vertex i and j

**Pros:** Quick to check if edge exists, good for dense graphs
**Cons:** Takes lots of space for sparse graphs

### 2. Adjacency List  
**What:** Each vertex has a list of its neighbors

**Pros:** Space efficient for sparse graphs, easy to add/remove edges
**Cons:** Slower to check if specific edge exists

### 3. Edge List
**What:** Simple list of all edges as pairs

**Pros:** Very simple, good for some algorithms
**Cons:** Slow for most operations

---

## Traversal Algorithms 🚶‍♂️

### Breadth-First Search (BFS)
**Think:** Exploring level by level, like ripples in a pond

**When to use:**
- Finding shortest path (unweighted graphs)
- Level-by-level processing
- Finding all nodes at distance k

**Key insight:** Uses a queue (FIFO - First In, First Out)

### Depth-First Search (DFS)  
**Think:** Go as deep as possible, then backtrack

**When to use:**
- Detecting cycles
- Topological sorting
- Finding connected components
- Maze solving

**Key insight:** Uses a stack (LIFO - Last In, First Out) or recursion

---

## Shortest Path Algorithms 🛣️

### For GATE DA, focus on these:

**BFS (Unweighted graphs)**
- Guaranteed shortest path
- Time: O(V + E)

**Dijkstra's Algorithm (Weighted graphs, non-negative weights)**
- Uses priority queue
- Time: O((V + E) log V)

**Bellman-Ford (Weighted graphs, can handle negative weights)**
- Can detect negative cycles
- Time: O(VE)

---

## Python Cheat Sheet 🐍

### Basic Graph Class
```python
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Adjacency list
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        # For undirected graph, also add:
        # self.graph[v].append(u)
```

### BFS Template
```python
def bfs(self, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

### DFS Template  
```python
def dfs(self, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []
        
    visited.add(start)
    result.append(start)
    
    for neighbor in self.graph[start]:
        if neighbor not in visited:
            self.dfs(neighbor, visited, result)
            
    return result
```

### Quick Adjacency Matrix
```python
def create_adj_matrix(edges, num_vertices):
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # For undirected graph
    return matrix
```

---

## GATE Exam Tips 🎯

### What You MUST Know:
1. **Basic definitions** - vertex, edge, degree, path, cycle
2. **BFS and DFS** - how they work, when to use each
3. **Graph representations** - adjacency list vs matrix trade-offs
4. **Simple shortest path** - BFS for unweighted graphs

### Common Question Types:
- Given a graph, perform BFS/DFS traversal
- Count vertices/edges in a graph
- Determine if a graph is connected
- Find shortest path between two vertices
- Identify cycles in a graph

### Memory Tricks:
- **BFS = Breadth = Queue** (wide search, FIFO)
- **DFS = Depth = Stack** (deep search, LIFO)
- **Matrix = Fast lookup, more space**
- **List = Less space, slower lookup**

### Quick Formulas:
- **Complete graph edges:** n(n-1)/2 (undirected), n(n-1) (directed)
- **Tree edges:** Always n-1 edges for n vertices
- **Handshaking lemma:** Sum of all degrees = 2 × number of edges

---

## Practice Problems 🏋️‍♀️

### Easy Warm-ups:
1. Given edges [(0,1), (1,2), (2,3)], draw the graph
2. Perform BFS starting from vertex 0
3. Convert adjacency list to adjacency matrix

### Medium Challenges:
1. Find if path exists between two vertices
2. Count number of connected components
3. Detect cycle in undirected graph

### GATE-Style:
1. What is the minimum number of edges to make a graph with 5 vertices connected?
2. In a BFS traversal, what data structure is used?
3. Time complexity of DFS for a graph with V vertices and E edges?

---

## Quick Reference Card 📋

```
GRAPH BASICS:
• Graph = (Vertices, Edges)
• Degree = number of edges from a vertex
• Path = sequence of connected vertices
• Cycle = path that returns to start

REPRESENTATIONS:
• Matrix: [i][j] = 1 if edge exists
• List: vertex → list of neighbors
• Edge List: [(u,v), (x,y), ...]

ALGORITHMS:
• BFS: Queue, level-by-level, shortest path (unweighted)
• DFS: Stack/recursion, go deep, detect cycles

TIME COMPLEXITY:
• BFS/DFS: O(V + E)
• Adjacency Matrix: O(1) lookup, O(V²) space
• Adjacency List: O(degree) lookup, O(V+E) space
```

Remember: Graphs are everywhere! Once you see the pattern, you'll spot them in social networks, transportation, web pages, and tons of other places. You've got this! 🌟