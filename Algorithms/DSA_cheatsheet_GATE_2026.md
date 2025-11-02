| **Category**              | **Algorithm / Concept**           | **Best / Avg / Worst Time**          | **Space** | **Stable** | **In-place**            | **Technique / Property**            | **Key Notes / Use Cases**                  | **GATE Importance** |
| ------------------------- | --------------------------------- | ------------------------------------ | --------- | ---------- | ----------------------- | ----------------------------------- | ------------------------------------------ | ------------------- |
| **Searching**             | **Linear Search**                 | O(1) / O(n) / O(n)                   | O(1)      | –          | –                       | Sequential                          | Works on unsorted arrays                   | ⭐⭐                  |
|                           | **Binary Search**                 | O(1) / O(log n) / O(log n)           | O(1)      | –          | Yes                     | Divide & Conquer                    | Works only on sorted arrays                | ⭐⭐⭐                 |
| **Sorting**               | **Selection Sort**                | O(n²) / O(n²) / O(n²)                | O(1)      | ❌          | ✅                       | Iterative                           | Minimum swaps; poor efficiency             | ⭐                   |
|                           | **Bubble Sort**                   | O(n) / O(n²) / O(n²)                 | O(1)      | ✅          | ✅                       | Iterative                           | Good for small lists or nearly sorted data | ⭐⭐                  |
|                           | **Insertion Sort**                | O(n) / O(n²) / O(n²)                 | O(1)      | ✅          | ✅                       | Incremental                         | Best for small / nearly sorted data        | ⭐⭐⭐                 |
|                           | **Merge Sort**                    | O(n log n) / O(n log n) / O(n log n) | O(n)      | ✅          | ❌                       | Divide & Conquer, Recursive         | Stable, used in external sorting           | ⭐⭐⭐                 |
|                           | **Quick Sort**                    | O(n log n) / O(n log n) / O(n²)      | O(log n)  | ❌          | ✅                       | Divide & Conquer, Recursive         | Fastest in practice, depends on pivot      | ⭐⭐⭐                 |
| **Divide & Conquer**      | **Binary Search**                 | O(log n)                             | O(1)      | –          | ✅                       | Recursion / D&C                     | Repeated halving of search space           | ⭐⭐⭐                 |
|                           | **Merge Sort**                    | O(n log n)                           | O(n)      | ✅          | ❌                       | Recursive / D&C                     | Splitting and merging subarrays            | ⭐⭐⭐                 |
|                           | **Quick Sort**                    | O(n log n)                           | O(log n)  | ❌          | ✅                       | Recursive / D&C                     | Random pivot gives good avg. performance   | ⭐⭐⭐                 |
| **Basic Data Structures** | **Array**                         | Access O(1), Search O(n)             | O(n)      | –          | –                       | Sequential                          | Fixed size, contiguous                     | ⭐⭐                  |
|                           | **Stack (LIFO)**                  | Push/Pop O(1)                        | O(n)      | –          | –                       | Abstract Data Type                  | Recursion, expression evaluation           | ⭐⭐⭐                 |
|                           | **Queue (FIFO)**                  | Enqueue/Dequeue O(1)                 | O(n)      | –          | –                       | Abstract Data Type                  | Scheduling, buffering                      | ⭐⭐⭐                 |
|                           | **Linked List (Singly)**          | Search O(n), Insert/Delete O(1)      | O(n)      | –          | –                       | Dynamic                             | No contiguous memory, flexible size        | ⭐⭐⭐                 |
|                           | **Doubly Linked List**            | Search O(n), Insert/Delete O(1)      | O(n)      | –          | –                       | Dynamic                             | Can traverse in both directions            | ⭐⭐                  |
|                           | **Hash Table**                    | Avg O(1), Worst O(n)                 | O(n)      | –          | –                       | Hashing                             | Collisions handled via chaining / probing  | ⭐⭐⭐⭐                |
| **Trees**                 | **Binary Search Tree (BST)**      | O(log n) / O(log n) / O(n)           | O(n)      | –          | –                       | Recursive                           | Inorder traversal gives sorted order       | ⭐⭐⭐                 |
|                           | **Balanced BST (AVL, Red-Black)** | O(log n)                             | O(n)      | –          | –                       | Rotation                            | Self-balancing BSTs                        | ⭐⭐⭐                 |
| **Graph Algorithms**      | **DFS**                           | O(V + E)                             | O(V)      | –          | –                       | Recursive / Stack                   | Detect cycles, topological sort            | ⭐⭐⭐                 |
|                           | **BFS**                           | O(V + E)                             | O(V)      | –          | –                       | Queue-based                         | Shortest path in unweighted graph          | ⭐⭐⭐                 |
|                           | **Dijkstra’s Algorithm**          | O((V + E) log V)                     | O(V)      | –          | –                       | Greedy                              | Shortest path (non-negative weights)       | ⭐⭐⭐⭐                |
|                           | **Topological Sort**              | O(V + E)                             | O(V)      | –          | –                       | DFS or BFS based                    | DAG ordering                               | ⭐⭐                  |
|                           | **Shortest Path (Unweighted)**    | O(V + E)                             | O(V)      | –          | –                       | BFS                                 | Equal edge weights assumed                 | ⭐⭐                  |
| **Graph Theory Basics**   | –                                 | –                                    | –         | –          | –                       | Adjacency List/Matrix               | Sparse vs Dense graphs, degree concepts    | ⭐⭐                  |
| **Algorithmic Paradigms** | **Divide and Conquer**            | O(n log n) typical                   | –         | –          | Recursive               | MergeSort, QuickSort, Binary Search | ⭐⭐⭐                                        |                     |
|                           | **Greedy**                        | Problem-dependent                    | –         | –          | Iterative               | Dijkstra, Kruskal, Prim             | ⭐⭐⭐                                        |                     |
|                           | **Dynamic Programming**           | Problem-dependent                    | –         | –          | Recursive + Memoization | Shortest path, knapsack, etc.       | ⭐⭐⭐⭐                                       |                     |
|                           | **Backtracking**                  | Exponential (O(2ⁿ))                  | –         | –          | Recursive               | N-Queens, Subset sum                | ⭐⭐                                         |                     |


| Algorithm         | Best Case | Average Case | Worst Case | Space Complexity | GATE Importance |
| ----------------- | --------- | ------------ | ---------- | ---------------- | --------------- |
| **Linear Search** | O(1)      | O(n)         | O(n)       | O(1)             | ⭐⭐              |
| **Binary Search** | O(1)      | O(log n)     | O(log n)   | O(1)             | ⭐⭐⭐             |

| Algorithm          | Best Case  | Average Case | Worst Case | Space Complexity | Stable? | GATE Importance |
| ------------------ | ---------- | ------------ | ---------- | ---------------- | ------- | --------------- |
| **Selection Sort** | O(n²)      | O(n²)        | O(n²)      | O(1)             | No      | ⭐               |
| **Bubble Sort**    | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes     | ⭐⭐              |
| **Insertion Sort** | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes     | ⭐⭐⭐             |
| **Merge Sort**     | O(n log n) | O(n log n)   | O(n log n) | O(n)             | Yes     | ⭐⭐⭐             |
| **Quick Sort**     | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | No      | ⭐⭐⭐             |

| Data Structure  | Access   | Search   | Insertion | Deletion | Space Complexity | GATE Importance |
| --------------- | -------- | -------- | --------- | -------- | ---------------- | --------------- |
| **Array**       | O(1)     | O(n)     | O(n)      | O(n)     | O(n)             | ⭐⭐              |
| **Stack**       | -        | -        | O(1)      | O(1)     | O(n)             | ⭐⭐⭐             |
| **Queue**       | -        | -        | O(1)      | O(1)     | O(n)             | ⭐⭐⭐             |
| **Linked List** | O(n)     | O(n)     | O(1)      | O(1)     | O(n)             | ⭐⭐⭐             |
| **Tree (BST)**  | O(log n) | O(log n) | O(log n)  | O(log n) | O(n)             | ⭐⭐⭐             |
| **Hash Table**  | O(1)     | O(1)     | O(1)      | O(1)     | O(n)             | ⭐⭐⭐⭐            |

| Algorithm / Concept            | Time Complexity  | Space Complexity | GATE Importance |
| ------------------------------ | ---------------- | ---------------- | --------------- |
| **DFS (Depth First Search)**   | O(V + E)         | O(V)             | ⭐⭐⭐             |
| **BFS (Breadth First Search)** | O(V + E)         | O(V)             | ⭐⭐⭐             |
| **Dijkstra’s Algorithm**       | O((V + E) log V) | O(V)             | ⭐⭐⭐⭐            |
| **Shortest Path (Unweighted)** | O(V + E)         | O(V)             | ⭐⭐⭐             |
| **Topological Sort**           | O(V + E)         | O(V)             | ⭐⭐              |

| Category             | Typical Time Complexity | Typical Space Complexity |
| -------------------- | ----------------------- | ------------------------ |
| **Searching**        | O(log n) – O(n)         | O(1)                     |
| **Sorting**          | O(n log n) – O(n²)      | O(1) – O(n)              |
| **Graph Traversal**  | O(V + E)                | O(V)                     |
| **Divide & Conquer** | O(n log n)              | O(n)                     |
| **Hashing**          | O(1) average            | O(n)                     |
