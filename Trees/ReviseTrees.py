# from collections import deque
#
# from anaconda_project.internal.conda_api import result
#
#
# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#
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
#     def insert_level_order(self,data):
#         new_node = TreeNode(data)
#         if self.root is None:
#             self.root = new_node
#             self.size += 1
#             print(f"New Node is the root: {data}")
#         queue = deque([self.root])
#         while queue:
#             current = queue.popleft()
#             if current.left is None:
#                 current.left = new_node
#                 self.size += 1
#                 print(f"New Node {data} inserted as the left child of {current.data}")
#             elif current.right is None:
#                 current.right = new_node
#                 self.size += 1
#                 print(f"New Node {data} inserted as the right child of {current.data}")
#             else:
#                 queue.append(current.left)
#                 queue.append(current.right)
#     def check_for_cycles(self,node=None,visited=None):
#         if visited is None:
#             visited = set()
#         if node is None:
#             node = self.root
#         if node is None:
#             return False
#         if id(node) in visited:
#             print(f"CYCLE DETECTED! Node {node.data} (id: {id(node)}) already visited")
#             return True
#         visited.add(id(node))
#         left_has_cycle = self.check_for_cycles(node.left,visited.copy()) if node.left else False
#         right_has_cycle = self.check_for_cycles(node.right, visited.copy()) if node.right else False
#         return left_has_cycle or right_has_cycle
#     def inorder_with_cycle_detection(self,node = None,visited=None,depth =0 ):
#         if visited is None:
#             visited = set()
#         if node is None:
#             node = self.root
#         if node is None:
#             return []
#         if depth > 20:
#             print(f"DEPTH LIMIT OF 20 REACHED AT NODE: {node.data} (depth {depth})")
#             return [f"DEPTH_LIMIT_AT_{node.data}"]
#         node_id = id(node)
#         if node_id in visited:
#             print(f"CYCLE DETECTED during traversal at node {node.data}!")
#             return  [f"CYCLE_AT_{node.data}"]
#         visited.add(node_id)
#         result = []
#         if node.left:
#             result.extend(self.inorder_with_cycle_detection(node.left,visited.copy(),depth+1))
#         result.append(self.root)
#         if node.right:
#             result.extend(self.inorder_with_cycle_detection(node.right,visited.copy(),depth+1))
#         return  result
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
            return

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

    def check_for_cycles(self, node=None, visited=None):
        """Check if tree has any circular references"""
        if visited is None:
            visited = set()

        if node is None:
            node = self.root

        if node is None:
            return False

        # If we've seen this node before, we have a cycle
        if id(node) in visited:
            print(f"CYCLE DETECTED! Node {node.data} (id: {id(node)}) already visited")
            return True

        visited.add(id(node))

        # Check left and right subtrees
        left_has_cycle = self.check_for_cycles(node.left, visited.copy()) if node.left else False
        right_has_cycle = self.check_for_cycles(node.right, visited.copy()) if node.right else False

        return left_has_cycle or right_has_cycle

    def safe_inorder_with_cycle_detection(self, node=None, visited=None, depth=0):
        """Inorder traversal with cycle detection and depth limit"""
        if visited is None:
            visited = set()

        if node is None:
            node = self.root

        if node is None:
            return []

        # Safety check: prevent infinite recursion
        if depth > 20:  # Reasonable depth limit
            print(f"DEPTH LIMIT REACHED at node {node.data} (depth {depth})")
            return [f"DEPTH_LIMIT_AT_{node.data}"]

        # Check for cycles
        node_id = id(node)
        if node_id in visited:
            print(f"CYCLE DETECTED during traversal at node {node.data}")
            return [f"CYCLE_AT_{node.data}"]

        visited.add(node_id)

        result = []

        # Left subtree
        if node.left:
            result.extend(self.safe_inorder_with_cycle_detection(node.left, visited.copy(), depth + 1))

        # Current node
        result.append(node.data)

        # Right subtree
        if node.right:
            result.extend(self.safe_inorder_with_cycle_detection(node.right, visited.copy(), depth + 1))

        return result

    def debug_tree_structure(self):
        """Debug the tree structure to find issues"""
        print("=== DEBUGGING TREE STRUCTURE ===")

        if self.root is None:
            print("Tree is empty")
            return

        print(f"Root: {self.root.data} (id: {id(self.root)})")

        # Check for cycles
        print("\n1. Checking for cycles...")
        has_cycles = self.check_for_cycles()
        if has_cycles:
            print("❌ CYCLES FOUND IN TREE!")
        else:
            print("✅ No cycles detected")

        # Check node relationships
        print("\n2. Node relationships:")
        queue = deque([self.root])
        level = 0

        while queue and level < 5:  # Limit to prevent infinite loop
            level_size = len(queue)
            print(f"Level {level}:")

            for i in range(level_size):
                node = queue.popleft()
                left_info = f"L:{node.left.data}(id:{id(node.left)})" if node.left else "L:None"
                right_info = f"R:{node.right.data}(id:{id(node.right)})" if node.right else "R:None"

                print(f"  Node {node.data}(id:{id(node)}) -> {left_info}, {right_info}")

                # Check for self-references
                if node.left == node:
                    print(f"  ❌ SELF-REFERENCE: Node {node.data} points to itself as left child!")
                if node.right == node:
                    print(f"  ❌ SELF-REFERENCE: Node {node.data} points to itself as right child!")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        print(f"\n3. Safe traversal attempt:")
        safe_result = self.safe_inorder_with_cycle_detection()
        print(f"Safe inorder result: {safe_result}")

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


if __name__ == "__main__":
    print("=== Binary Tree Debug Session ===\n")

    # Create tree
    bt = BinaryTree()

    # Insert nodes
    for i in [1, 2, 3, 4, 5, 6, 7]:
        bt.insert_level_order(i)

    print("\n" + "=" * 50)

    # Debug the tree structure
    bt.debug_tree_structure()

    print("\n" + "=" * 50)
    print("Attempting normal inorder traversal...")

    try:
        result = bt.inorder_recursive()
        print(f"SUCCESS! Inorder result: {result}")
    except RecursionError as e:
        print(f"❌ RECURSION ERROR: {e}")
        print("This confirms there's a circular reference in the tree structure.")