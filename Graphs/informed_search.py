import heapq
import math

class AOStar:
    """
    AO* Search for AND-OR graphs
    
    Use cases:
    - Planning problems with subgoals
    - Game playing (minimax-like)
    - Problem decomposition
    
    AND nodes: Must solve ALL children
    OR nodes: Need to solve only ONE child
    """
    
    def __init__(self,graph,heuristic,and_nodes):
        self.graph = graph
        self.heuristic = heuristic
        self.and_nodes = and_nodes
        self.solution_graph = []
        self.solved = set()
        self.cost_memo = {}

    def is_solved(self,node,goal):
        if node == goal:
            return True
        if node not in self.solution_graph:
            return False
        if node in self.and_node:
            return all(self.is_solved(child,goal) for child in self.solution_graph[node])
    def compute_cost(self,node,goal)    :
        if node in self.cost_memo:
            return self.cost_memo[node]
        if node == goal:
            return 0 
        if node not in self.solution_graph:
            return float('inf')
        if node in self.and_nodes:
            total = 0
            for child in self.solution_graph[node]:
                edge_cost = self.graph[node].get(child,float('inf'))
                child_cost = self.compute_cost(child,goal)
                total += edge_cost + child_cost
        else:
            total = float('inf')
            for child in self.solution_graph[node]:
                edge_cost = self.graph[node].get(child,float('inf'))
                child_cost = self.compute_cost(child_cost,goal)
                total = min(total,edge_cost+child_cost)
            self.cost_memo[node] = total
            return total
    def search(self, start, goal):
        """Main AO* search algorithm"""
        open_list = [(self.heuristic[start], start)]
        
        print("\n=== AO* SEARCH ===")
        
        while open_list and not self.is_solved(start, goal):
            _, node = heapq.heappop(open_list)
            
            if node == goal:
                self.solved.add(node)
                continue
            
            node_type = "AND" if node in self.and_nodes else "OR"
            print(f"Expanding: {node:10} | Type: {node_type:3} | h={self.heuristic[node]:5.1f}")
            
            # Select successors based on node type
            if node in self.and_nodes:
                # AND node: must include ALL children
                self.solution_graph[node] = list(self.graph.get(node, {}).keys())
            else:
                # OR node: choose best child by f = cost + heuristic
                children = self.graph.get(node, {})
                if children:
                    best_child = min(
                        children.keys(),
                        key=lambda c: children[c] + self.heuristic[c]
                    )
                    self.solution_graph[node] = [best_child]
            
            # Clear cost memo when graph changes
            self.cost_memo = {}
            
            # Add unexplored children to open list
            for child in self.solution_graph.get(node, []):
                if not self.is_solved(child, goal):
                    f = self.compute_cost(start, goal) + self.heuristic[child]
                    heapq.heappush(open_list, (f, child))
        
        if self.is_solved(start, goal):
            cost = self.compute_cost(start, goal)
            print(f"\n✓ Solution found! Cost: {cost}")
            print(f"Solution graph: {self.solution_graph}")
            return self.solution_graph, cost
        
        return None, float('inf')



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
# if __name__ == "__main__":
#     # Graph for Greedy and A*
#     ao_solver = AOStar()
#     graph = {
#         'S': [('A', 1), ('B', 4)],
#         'A': [('C', 2), ('E', 12)],
#         'B': [('D', 2)],
#         'C': [('E', 3), ('G', 15)],
#         'D': [('G', 1)],
#         'E': [('G', 2)],
#         'G': []
#     }
    
#     # Node positions for heuristic calculation
#     positions = {
#         'S': (0, 0),
#         'A': (1, 2),
#         'B': (1, -1),
#         'C': (2, 1),
#         'D': (2, -2),
#         'E': (3, 2),
#         'G': (4, 0)
#     }
    
#     # Calculate heuristic (straight-line distance to goal)
#     goal_pos = positions['G']
#     heuristic = {
#         node: euclidean_distance(pos, goal_pos) 
#         for node, pos in positions.items()
#     }
    
#     print("Heuristic values (distance to goal):")
#     for node, h in sorted(heuristic.items()):
#         print(f"  h({node}) = {h:.2f}")
#     print()
    
#     # Run Greedy Best-First
#     path1, cost1 = greedy_best_first(graph, 'S', 'G', heuristic)
#     print(f"Total cost: {cost1}\n")
    
#     # Run A*
#     path2, cost2 = a_star(graph, 'S', 'G', heuristic)
#     print(f"Total cost: {cost2}\n")
    
#     print("=" * 50)
#     print(f"COMPARISON:")
#     print(f"Greedy path: {' -> '.join(path1) if path1 else 'Not found'} | Cost: {cost1}")
#     print(f"A* path:     {' -> '.join(path2) if path2 else 'Not found'} | Cost: {cost2}")
#     print(f"A* found optimal: {cost2 <= cost1}")
#     print("=" * 50)
    
#     # AO* Example: Robot assembly task
#     print("\n\n" + "=" * 50)
#     print("AO* EXAMPLE: Robot Assembly Task")
#     print("=" * 50)
    
#     graph_ao = {
#         'START': {'GET_PART1': 2, 'GET_PART2': 3},
#         'GET_PART1': {'PART1_A': 1, 'PART1_B': 4},
#         'GET_PART2': {'PART2_A': 2, 'PART2_B': 5},
#         'PART1_A': {'ASSEMBLE': 1},
#         'PART1_B': {'ASSEMBLE': 1},
#         'PART2_A': {'ASSEMBLE': 1},
#         'PART2_B': {'ASSEMBLE': 2},
#         'ASSEMBLE': {'GOAL': 0},
#         'GOAL': {}
#     }
    
#     heuristic_ao = {
#         'START': 6,
#         'GET_PART1': 3,
#         'GET_PART2': 3,
#         'PART1_A': 2,
#         'PART1_B': 2,
#         'PART2_A': 2,
#         'PART2_B': 2,
#         'ASSEMBLE': 1,
#         'GOAL': 0
#     }
    
#     # START is AND node: must complete BOTH GET_PART1 AND GET_PART2
#     and_nodes = {'START'}
    
#     # ao_solver = AOStar(graph_ao, heuristic_ao, and_nodes)
#     solution, cost = ao_solver.search('START', 'GOAL')
    
#     print("\n" + "=" * 50)
#     print("KEY TAKEAWAYS:")
#     print("=" * 50)
#     print("1. Greedy: Fast but NOT optimal (uses only h(n))")
#     print("2. A*: Optimal with admissible heuristic (g(n) + h(n))")
#     print("3. AO*: Handles AND/OR decomposition (complex problems)")
#     print("=" * 50)


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
    
    print("=" * 50)
    print(f"COMPARISON:")
    print(f"Greedy path: {' -> '.join(path1) if path1 else 'Not found'} | Cost: {cost1}")
    print(f"A* path:     {' -> '.join(path2) if path2 else 'Not found'} | Cost: {cost2}")
    print(f"A* found optimal: {cost2 <= cost1}")
    print("=" * 50)
    
    # AO* Example: Robot assembly task
    print("\n\n" + "=" * 50)
    print("AO* EXAMPLE: Robot Assembly Task")
    print("=" * 50)
    
    graph_ao = {
        'START': {'GET_PART1': 2, 'GET_PART2': 3},
        'GET_PART1': {'PART1_A': 1, 'PART1_B': 4},
        'GET_PART2': {'PART2_A': 2, 'PART2_B': 5},
        'PART1_A': {'ASSEMBLE': 1},
        'PART1_B': {'ASSEMBLE': 1},
        'PART2_A': {'ASSEMBLE': 1},
        'PART2_B': {'ASSEMBLE': 2},
        'ASSEMBLE': {'GOAL': 0},
        'GOAL': {}
    }
    
    heuristic_ao = {
        'START': 6,
        'GET_PART1': 3,
        'GET_PART2': 3,
        'PART1_A': 2,
        'PART1_B': 2,
        'PART2_A': 2,
        'PART2_B': 2,
        'ASSEMBLE': 1,
        'GOAL': 0
    }
    
    # START is AND node: must complete BOTH GET_PART1 AND GET_PART2
    and_nodes = {'START'}
    
    ao_solver = AOStar(graph_ao, heuristic_ao, and_nodes)
    solution, cost = ao_solver.search('START', 'GOAL')
    
    print("\n" + "=" * 50)
    print("KEY TAKEAWAYS:")
    print("=" * 50)
    print("1. Greedy: Fast but NOT optimal (uses only h(n))")
    print("2. A*: Optimal with admissible heuristic (g(n) + h(n))")
    print("3. AO*: Handles AND/OR decomposition (complex problems)")
    print("=" * 50)

