import heapq
import math

def euclidean_distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]+p2[1])**2)
def greedy_best_first(graph,root,target,heuristic):
    print(f"Using GBFS - only heuristic formula: f(n) = h(n)")
    visited = set()
    pq = [(heuristic[root],root,[root],0)]
    while pq:
        h,node,path,cost = heapq.heappop(pq)
        if node == target:
            return path,cost
        if node in visited:
            continue
        visited.add(node)
        for neighbour,edge_cost in graph.get(node,[]):
            if neighbour not in visited:
                h_neighbour =  heuristic[neighbour]
                new_path = path+[node]
                new_cost = cost+edge_cost
                heapq.heappush(pq,(h_neighbour,neighbour,new_path,new_cost))
    return None,float('-inf')

def a_star(graph,root,target,heuristic):
    print(f"Using A* - only heuristic formula: f(n) = g(n) + h(n)")
    visited = {}
    # Priority queue: (f(n), g(n), node, path)
    pq = [(heuristic[root],0,root,[root])]
    while pq:
        f,g,node,path = heapq.heappop(pq)
        if node == target:
            return path, g
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        h = heuristic[node]
        for neighbour,edge_cost in graph.get(node,[]):
            if neighbour not in visited:
                new_g = g+edge_cost
                new_h = heuristic[neighbour]
                new_f = new_g + new_h
                if neighbour not in visited or visited[neighbour] > new_g:
                    new_path = path + [neighbour]
                    heapq.heappush(pq,(new_f,new_g,neighbour,new_path))
    return None,float('-inf')
if __name__ == "__main__":
    # Graph for Greedy and A*
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 2), ('E', 12)],
        'B': [('D', 2)],
        'C': [('E', 3), ('G', 15)],
        'D': [('G', 1)],
        'E': [('G', 2)],
        'G': []
    }
    
    # Node positions for heuristic calculation
    positions = {
        'S': (0, 0),
        'A': (1, 2),
        'B': (1, -1),
        'C': (2, 1),
        'D': (2, -2),
        'E': (3, 2),
        'G': (4, 0)
    }
    
    # Calculate heuristic (straight-line distance to goal)
    goal_pos = positions['G']
    heuristic = {
        node: euclidean_distance(pos, goal_pos) 
        for node, pos in positions.items()
    }
    
    print("Heuristic values (distance to goal):")
    for node, h in sorted(heuristic.items()):
        print(f"  h({node}) = {h:.2f}")
    print()
    
    # Run Greedy Best-First
    path1, cost1 = greedy_best_first(graph, 'S', 'G', heuristic)
    print(f"Total cost: {cost1}\n")
    
    # Run A*
    path2, cost2 = a_star(graph, 'S', 'G', heuristic)
    print(f"Total cost: {cost2}\n")
    
    # print("=" * 50)
    # print(f"COMPARISON:")
    # print(f"Greedy path: {' -> '.join(path1) if path1 else 'Not found'} | Cost: {cost1}")
    # print(f"A* path:     {' -> '.join(path2) if path2 else 'Not found'} | Cost: {cost2}")
    # print(f"A* found optimal: {cost2 <= cost1}")
    # print("=" * 50)
    
    # # AO* Example: Robot assembly task
    # print("\n\n" + "=" * 50)
    # print("AO* EXAMPLE: Robot Assembly Task")
    # print("=" * 50)
    
    # graph_ao = {
    #     'START': {'GET_PART1': 2, 'GET_PART2': 3},
    #     'GET_PART1': {'PART1_A': 1, 'PART1_B': 4},
    #     'GET_PART2': {'PART2_A': 2, 'PART2_B': 5},
    #     'PART1_A': {'ASSEMBLE': 1},
    #     'PART1_B': {'ASSEMBLE': 1},
    #     'PART2_A': {'ASSEMBLE': 1},
    #     'PART2_B': {'ASSEMBLE': 2},
    #     'ASSEMBLE': {'GOAL': 0},
    #     'GOAL': {}
    # }
    
    # heuristic_ao = {
    #     'START': 6,
    #     'GET_PART1': 3,
    #     'GET_PART2': 3,
    #     'PART1_A': 2,
    #     'PART1_B': 2,
    #     'PART2_A': 2,
    #     'PART2_B': 2,
    #     'ASSEMBLE': 1,
    #     'GOAL': 0
    # }
    
    # # START is AND node: must complete BOTH GET_PART1 AND GET_PART2
    # and_nodes = {'START'}
    
    # # ao_solver = AOStar(graph_ao, heuristic_ao, and_nodes)
    # solution, cost = ao_solver.search('START', 'GOAL')
    
    # print("\n" + "=" * 50)
    # print("KEY TAKEAWAYS:")
    # print("=" * 50)
    # print("1. Greedy: Fast but NOT optimal (uses only h(n))")
    # print("2. A*: Optimal with admissible heuristic (g(n) + h(n))")
    # print("3. AO*: Handles AND/OR decomposition (complex problems)")
    # print("=" * 50)