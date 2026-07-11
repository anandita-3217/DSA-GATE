# Trees, Graphs & Path-Finding Algorithms — Study Notes

---

## 1. Trees

A **tree** is a connected, acyclic graph with `N` nodes and `N-1` edges. There's exactly one path between any two nodes.

**Key terms**
- **Root**: top node (in rooted trees)
- **Parent / Child**: direct relationship
- **Leaf**: node with no children
- **Height**: longest path from a node down to a leaf
- **Depth**: distance from root to a node
- **Subtree**: a node plus all its descendants

**Common types**
- General tree (any number of children)
- Binary tree (≤2 children per node)
- Binary Search Tree (BST)
- Balanced trees: AVL, Red-Black
- Heap (complete binary tree, heap-order property)
- Trie (prefix tree for strings)

---

## 2. Binary Trees

Each node has at most **left** and **right** children.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### Traversals

| Type | Order | Use case |
|---|---|---|
| Preorder | Root → Left → Right | Copy/serialize tree |
| Inorder | Left → Root → Right | Sorted output (BST) |
| Postorder | Left → Right → Root | Delete tree, evaluate expr |
| Level-order (BFS) | Level by level | Shortest structural distance |

```python
def inorder(node, out):
    if not node: return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)

def level_order(root):
    from collections import deque
    q, out = deque([root]), []
    while q:
        node = q.popleft()
        if not node: continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    return out
```

### Binary Search Tree (BST)
Property: `left subtree < node < right subtree`.

- Search / Insert / Delete: **O(log n)** average, **O(n)** worst case (skewed tree)
- Balanced variants (AVL, Red-Black) guarantee **O(log n)** worst case via rotations.

### Complexity Summary

| Operation | BST (avg) | BST (worst) | Balanced BST |
|---|---|---|---|
| Search | O(log n) | O(n) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |

---

## 3. Graphs

A **graph** `G = (V, E)` — set of vertices and edges. Can be:
- **Directed / Undirected**
- **Weighted / Unweighted**
- **Cyclic / Acyclic**

### Representations

**Adjacency list** (most common, space-efficient for sparse graphs)
```python
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}
```
Space: O(V + E)

**Adjacency matrix** — good for dense graphs, O(1) edge lookup, O(V²) space.

### Traversals

**BFS** — explores level by level, uses a queue. Finds shortest path in *unweighted* graphs.
```python
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
Time: O(V + E)

**DFS** — explores as deep as possible, uses a stack (or recursion). Good for cycle detection, topological sort, connected components.
```python
def dfs(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```
Time: O(V + E)

---

## 4. Shortest Path Algorithms

### Dijkstra's Algorithm
Finds shortest path from a **single source** to all other nodes. Works only with **non-negative** edge weights.

**Idea**: Greedily pick the unvisited node with the smallest known distance, relax its neighbors, repeat. Uses a min-heap (priority queue).

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue  # stale entry
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist
```

- **Time**: O((V + E) log V) with a binary heap
- **Space**: O(V)
- **Limitation**: fails with negative weights (use Bellman-Ford instead)

### Bellman-Ford (for comparison)
Handles negative weights, detects negative cycles. O(V·E) time — slower but more general.

### A* Search
Like Dijkstra but uses a heuristic `h(n)` estimating distance to goal:
`f(n) = g(n) + h(n)`. Faster in practice for point-to-point search (e.g., maps/games) when heuristic is admissible (never overestimates).

---

## 5. Minimum Spanning Tree (MST) Algorithms

An MST connects all vertices of a weighted, undirected, connected graph with the **minimum total edge weight**, using exactly `V-1` edges and no cycles.

### Kruskal's Algorithm
**Edge-based** greedy approach. Good for sparse graphs.

**Idea**: Sort all edges by weight. Add the smallest edge if it doesn't form a cycle (checked using **Union-Find / Disjoint Set Union**).

```python
def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return True

def kruskal(vertices, edges):
    # edges: list of (weight, u, v)
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    mst = []
    for weight, u, v in sorted(edges):
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
    return mst
```

- **Time**: O(E log E) — dominated by sorting
- **Space**: O(V) for Union-Find

### Prim's Algorithm
**Vertex-based** greedy approach. Good for dense graphs.

**Idea**: Start from any node, grow the MST one edge at a time by always picking the cheapest edge connecting the tree to a new vertex. Uses a min-heap.

```python
def prim(graph, start):
    visited = {start}
    edges = [(w, start, to) for to, w in graph[start]]
    heapq.heapify(edges)
    mst = []

    while edges and len(visited) < len(graph):
        w, frm, to = heapq.heappop(edges)
        if to in visited:
            continue
        visited.add(to)
        mst.append((frm, to, w))
        for next_to, weight in graph[to]:
            if next_to not in visited:
                heapq.heappush(edges, (weight, to, next_to))
    return mst
```

- **Time**: O(E log V) with binary heap
- **Space**: O(V + E)

### Kruskal vs Prim

| | Kruskal | Prim |
|---|---|---|
| Approach | Edge-based | Vertex-based |
| Data structure | Union-Find | Min-heap |
| Best for | Sparse graphs | Dense graphs |
| Time | O(E log E) | O(E log V) |
| Builds | Possibly disconnected forest until end | Always one connected tree |

---

## 6. Quick Comparison Table

| Algorithm | Problem Solved | Graph Type | Time Complexity |
|---|---|---|---|
| BFS | Shortest path (unweighted) | Any | O(V+E) |
| DFS | Traversal, cycle detection | Any | O(V+E) |
| Dijkstra | Single-source shortest path | Non-negative weights | O((V+E) log V) |
| Bellman-Ford | Single-source shortest path | Negative weights allowed | O(V·E) |
| Kruskal | MST | Weighted, undirected | O(E log E) |
| Prim | MST | Weighted, undirected | O(E log V) |

---

## 7. Common Interview/Practice Problems
- Lowest Common Ancestor (LCA) in a binary tree
- Diameter of a binary tree
- Validate a BST
- Serialize/deserialize a binary tree
- Number of connected components
- Detect cycle in directed/undirected graph
- Topological sort (Kahn's algorithm / DFS-based)
- Network delay time (Dijkstra application)
- Min cost to connect all points (MST application)
