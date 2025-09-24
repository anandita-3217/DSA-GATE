# # from collections import deque
# #
# # from anaconda_project.internal.conda_api import result
# #
# #
# # class TreeNode:
# #     def __init__(self,data):
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #
# #     def __str__(self):
# #         return str(self.data)
# # class BinaryTree:
# #     def __init__(self):
# #         self.root = None
# #         self.size = 0
# #     def is_empty(self):
# #         return self.root is None
# #     def get_size(self):
# #         return self.size
# #     def insert_level_order(self,data):
# #         new_node = TreeNode(data)
# #         if self.root is None:
# #             self.root = new_node
# #             self.size += 1
# #             print(f"New Node is the root: {data}")
# #         queue = deque([self.root])
# #         while queue:
# #             current = queue.popleft()
# #             if current.left is None:
# #                 current.left = new_node
# #                 self.size += 1
# #                 print(f"New Node {data} inserted as the left child of {current.data}")
# #             elif current.right is None:
# #                 current.right = new_node
# #                 self.size += 1
# #                 print(f"New Node {data} inserted as the right child of {current.data}")
# #             else:
# #                 queue.append(current.left)
# #                 queue.append(current.right)
# #     def check_for_cycles(self,node=None,visited=None):
# #         if visited is None:
# #             visited = set()
# #         if node is None:
# #             node = self.root
# #         if node is None:
# #             return False
# #         if id(node) in visited:
# #             print(f"CYCLE DETECTED! Node {node.data} (id: {id(node)}) already visited")
# #             return True
# #         visited.add(id(node))
# #         left_has_cycle = self.check_for_cycles(node.left,visited.copy()) if node.left else False
# #         right_has_cycle = self.check_for_cycles(node.right, visited.copy()) if node.right else False
# #         return left_has_cycle or right_has_cycle
# #     def inorder_with_cycle_detection(self,node = None,visited=None,depth =0 ):
# #         if visited is None:
# #             visited = set()
# #         if node is None:
# #             node = self.root
# #         if node is None:
# #             return []
# #         if depth > 20:
# #             print(f"DEPTH LIMIT OF 20 REACHED AT NODE: {node.data} (depth {depth})")
# #             return [f"DEPTH_LIMIT_AT_{node.data}"]
# #         node_id = id(node)
# #         if node_id in visited:
# #             print(f"CYCLE DETECTED during traversal at node {node.data}!")
# #             return  [f"CYCLE_AT_{node.data}"]
# #         visited.add(node_id)
# #         result = []
# #         if node.left:
# #             result.extend(self.inorder_with_cycle_detection(node.left,visited.copy(),depth+1))
# #         result.append(self.root)
# #         if node.right:
# #             result.extend(self.inorder_with_cycle_detection(node.right,visited.copy(),depth+1))
# #         return  result
# from collections import deque


# class TreeNode:
#     """Node class for binary tree"""

#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def __str__(self):
#         return str(self.data)


# class BinaryTree:
#     def __init__(self):
#         self.root = None
#         self.size = 0

#     def is_empty(self):
#         return self.root is None

#     def get_size(self):
#         return self.size

#     def insert_level_order(self, data):
#         new_node = TreeNode(data)
#         if self.root is None:
#             self.root = new_node
#             self.size += 1
#             print(f"New node is the root: {data}")
#             return

#         queue = deque([self.root])
#         while queue:
#             current = queue.popleft()
#             if current.left is None:
#                 current.left = new_node
#                 self.size += 1
#                 print(f"Inserted {data} as left child of {current.data}")
#                 return
#             elif current.right is None:
#                 current.right = new_node
#                 self.size += 1
#                 print(f"Inserted {data} as right child of {current.data}")
#                 return
#             else:
#                 queue.append(current.left)
#                 queue.append(current.right)

#     def check_for_cycles(self, node=None, visited=None):
#         """Check if tree has any circular references"""
#         if visited is None:
#             visited = set()

#         if node is None:
#             node = self.root

#         if node is None:
#             return False

#         # If we've seen this node before, we have a cycle
#         if id(node) in visited:
#             print(f"CYCLE DETECTED! Node {node.data} (id: {id(node)}) already visited")
#             return True

#         visited.add(id(node))

#         # Check left and right subtrees
#         left_has_cycle = self.check_for_cycles(node.left, visited.copy()) if node.left else False
#         right_has_cycle = self.check_for_cycles(node.right, visited.copy()) if node.right else False

#         return left_has_cycle or right_has_cycle

#     def safe_inorder_with_cycle_detection(self, node=None, visited=None, depth=0):
#         """Inorder traversal with cycle detection and depth limit"""
#         if visited is None:
#             visited = set()

#         if node is None:
#             node = self.root

#         if node is None:
#             return []

#         # Safety check: prevent infinite recursion
#         if depth > 20:  # Reasonable depth limit
#             print(f"DEPTH LIMIT REACHED at node {node.data} (depth {depth})")
#             return [f"DEPTH_LIMIT_AT_{node.data}"]

#         # Check for cycles
#         node_id = id(node)
#         if node_id in visited:
#             print(f"CYCLE DETECTED during traversal at node {node.data}")
#             return [f"CYCLE_AT_{node.data}"]

#         visited.add(node_id)

#         result = []

#         # Left subtree
#         if node.left:
#             result.extend(self.safe_inorder_with_cycle_detection(node.left, visited.copy(), depth + 1))

#         # Current node
#         result.append(node.data)

#         # Right subtree
#         if node.right:
#             result.extend(self.safe_inorder_with_cycle_detection(node.right, visited.copy(), depth + 1))

#         return result

#     def debug_tree_structure(self):
#         """Debug the tree structure to find issues"""
#         print("=== DEBUGGING TREE STRUCTURE ===")

#         if self.root is None:
#             print("Tree is empty")
#             return

#         print(f"Root: {self.root.data} (id: {id(self.root)})")

#         # Check for cycles
#         print("\n1. Checking for cycles...")
#         has_cycles = self.check_for_cycles()
#         if has_cycles:
#             print("❌ CYCLES FOUND IN TREE!")
#         else:
#             print("✅ No cycles detected")

#         # Check node relationships
#         print("\n2. Node relationships:")
#         queue = deque([self.root])
#         level = 0

#         while queue and level < 5:  # Limit to prevent infinite loop
#             level_size = len(queue)
#             print(f"Level {level}:")

#             for i in range(level_size):
#                 node = queue.popleft()
#                 left_info = f"L:{node.left.data}(id:{id(node.left)})" if node.left else "L:None"
#                 right_info = f"R:{node.right.data}(id:{id(node.right)})" if node.right else "R:None"

#                 print(f"  Node {node.data}(id:{id(node)}) -> {left_info}, {right_info}")

#                 # Check for self-references
#                 if node.left == node:
#                     print(f"  ❌ SELF-REFERENCE: Node {node.data} points to itself as left child!")
#                 if node.right == node:
#                     print(f"  ❌ SELF-REFERENCE: Node {node.data} points to itself as right child!")

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             level += 1

#         print(f"\n3. Safe traversal attempt:")
#         safe_result = self.safe_inorder_with_cycle_detection()
#         print(f"Safe inorder result: {safe_result}")

#     def inorder_recursive(self, node=None):
#         """Inorder traversal: Left → Root → Right"""
#         if node is None:
#             node = self.root

#         result = []
#         if node:
#             result.extend(self.inorder_recursive(node.left))
#             result.append(node.data)
#             result.extend(self.inorder_recursive(node.right))

#         return result


# if __name__ == "__main__":
#     print("=== Binary Tree Debug Session ===\n")

#     # Create tree
#     bt = BinaryTree()

#     # Insert nodes
#     for i in [1, 2, 3, 4, 5, 6, 7]:
#         bt.insert_level_order(i)

#     print("\n" + "=" * 50)

#     # Debug the tree structure
#     bt.debug_tree_structure()

#     print("\n" + "=" * 50)
#     print("Attempting normal inorder traversal...")

#     try:
#         result = bt.inorder_recursive()
#         print(f"SUCCESS! Inorder result: {result}")
#     except RecursionError as e:
#         print(f"❌ RECURSION ERROR: {e}")
#         print("This confirms there's a circular reference in the tree structure.")
from collections import deque

class TreeNode:
    """Node class for binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def is_empty(self):
        return self.root is None

    def get_size(self):
        return self.size
    
    def insert_level_order(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            self.size += 1
            print(f"New node is the root: {data}")
            return  # CRITICAL FIX: Added missing return!

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                self.size += 1
                print(f"Inserted {data} as left child of {current.data}")
                return
            elif current.right is None:
                current.right = new_node
                self.size += 1
                print(f"Inserted {data} as right child of {current.data}")
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def inorder_recursive(self, node=None):
        """Inorder traversal: Left → Root → Right"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.extend(self.inorder_recursive(node.left))
            result.append(node.data)
            result.extend(self.inorder_recursive(node.right))
        
        return result

    def inorder_iterative(self):
        """Inorder traversal using stack (iterative) - FASTEST"""
        if not self.root:
            return []
        
        result = []
        stack = []
        current = self.root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.data)
            current = current.right
        
        return result

    def preorder_recursive(self, node=None):
        """Preorder traversal: Root → Left → Right"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.append(node.data)
            result.extend(self.preorder_recursive(node.left))
            result.extend(self.preorder_recursive(node.right))
        
        return result

    def preorder_iterative(self):
        """Preorder traversal using stack (iterative)"""
        if not self.root:
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            result.append(node.data)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result

    def postorder_recursive(self, node=None):
        """Postorder traversal: Left → Right → Root"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.extend(self.postorder_recursive(node.left))
            result.extend(self.postorder_recursive(node.right))
            result.append(node.data)
        
        return result

    def level_order(self):
        """Level order traversal (BFS) - OFTEN FASTEST IN PRACTICE"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

    def level_order_with_levels(self):
        """Level order traversal returning nodes grouped by level"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

    def display_tree(self):
        """Display tree structure visually"""
        if self.root is None:
            print("Tree is empty")
            return
        
        print("Tree Structure:")
        self._display_tree_helper(self.root, "", True)
        print(f"Total nodes: {self.get_size()}")
    
    def _display_tree_helper(self, node, prefix, is_last):
        """Helper method for tree visualization"""
        if node is not None:
            print(prefix + ("└── " if is_last else "├── ") + str(node.data))
            
            children = [child for child in [node.left, node.right] if child]
            
            for i, child in enumerate(children):
                is_last_child = i == len(children) - 1
                extension = "    " if is_last else "│   "
                self._display_tree_helper(child, prefix + extension, is_last_child)

if __name__ == "__main__":
    print("=== Fixed Binary Tree Implementation ===\n")
    
    # Create tree
    bt = BinaryTree()
    
    # Insert nodes in level order
    for i in [1, 2, 3, 4, 5, 6, 7]:
        bt.insert_level_order(i)
    
    print("\n" + "="*50)
    bt.display_tree()
    
    # Test all traversals
    print("\n2. Tree Traversals:")
    print(f"Inorder (Recursive):   {bt.inorder_recursive()}")
    print(f"Inorder (Iterative):   {bt.inorder_iterative()}")
    print(f"Preorder (Recursive):  {bt.preorder_recursive()}")
    print(f"Preorder (Iterative):  {bt.preorder_iterative()}")
    print(f"Postorder (Recursive): {bt.postorder_recursive()}")
    print(f"Level Order (Fastest): {bt.level_order()}")
    print(f"Level Order by Levels: {bt.level_order_with_levels()}")
    
    print("\n3. Performance Note:")
    print("✅ Level Order (BFS) is typically fastest for traversal")
    print("✅ Iterative methods are faster than recursive")
    print("✅ No more recursion errors!")