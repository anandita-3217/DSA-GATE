from collections import deque
import heapq

def dfs(graph,root,visited=None):
    if visited is None:
        visited = set()
    visited.add(root)
    for neighbour in graph.get(root,[]):
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
    return visited
def bfs (graph,root):
    visited = set()
    queue = deque([root])
    visited.add(root)
    while queue:
        cur = queue.popleft()
        print(f"Visiting node: {cur}")
        for neighbour in graph.get(cur,[]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return  visited
def iddfs_graph(graph, start, target, max_depth=float('inf')):
    """
    Iterative Deepening DFS - finds target node.
    
    Args:
        graph: adjacency list
        start: starting node
        target: node to find
        max_depth: maximum depth to search
    
    Returns:
        depth at which target was found, or -1 if not found
    """
    # Try increasing depth limits
    # for depth_limit in range(max_depth + 1):
    #     print(f"\n--- Trying depth limit: {depth_limit} ---")
    #     visited = set()
    #     found = dls(graph, start, target, depth_limit, visited)
    #     if found:
    #         return depth_limit
    
    # return -1  # Not found
    for depth_limit in range(max_depth+1):
        visited = set()
        found = dls(graph,start,target,depth_limit-1,visited)
        if found:
            return depth_limit
    return -1


def dls(graph, node, target, depth_limit, visited):
    """
    Depth-Limited Search (helper for IDDFS).
    
    Args:
        graph: adjacency list
        node: current node
        target: node to find
        depth_limit: maximum depth allowed
        visited: set of visited nodes at current depth path
    
    Returns:
        True if target found, False otherwise
    """
    print(f"Node: {node}, Current depth: {depth_limit}")
    if node == target:
        return True
    if depth_limit == 0:
        return False
    visited.add(node)
    for neighbour in graph.get(node,[]):
        if neighbour not in visited:
            if dls(graph,neighbour,target,depth_limit -1,visited):
                return True
    visited.remove(node)
    return False

def ucs(graph,root,target):
    pq = [(0,root,[root])]
    visited = set()
    while pq:
        cost,node,path = heapq.heappop(pq)
        if node == target:
            return path,cost
        if node in visited:
            continue
        visited.add(node)
        # print(f"Expanding: {node} | Cost so far: {cost} | Path: {path}")

        for neighbour,edge_cost in graph.get(node,[]):
            if neighbour not in visited:
                new_cost = cost+edge_cost
                new_path = path+[neighbour]
                heapq.heappush(pq,(new_cost,neighbour,new_path))
    return None,float('inf')

if __name__ == "__main__":
#     graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': ['H'],
#     'F': [],
#     'G': [],
#     'H': []
# }

    # fin_d = dfs(graph, 'A')
    # print(f"All visited nodes in dfs: {fin_d}")

    # fin_b = bfs(graph, 'A')
    # print(f"All visited nodes in bfs: {fin_b}")

    # depth = iddfs_graph(graph, 'A', 'H', max_depth=10)
    # print(f"\nFound 'H' at depth: {depth}")

    weighted_graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 2), ('G', 1)],
        'D': [('H', 3)],
        'E': [('H', 1)],
        'F': [],
        'G': [('H', 2)],
        'H': []
    }

    path, cost = ucs(weighted_graph, 'A', 'H')
    print(f"\n✓ Shortest path: {' -> '.join(path)}")
    print(f"✓ Total cost: {cost}")

