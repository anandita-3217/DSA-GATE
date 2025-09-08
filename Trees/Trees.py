from collections import deque


class Node:
    def __init__(self,data = 0,right = None,left = None):
        """Node class for binary tree"""
        self.data = data 
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

# class BinaryTree:
#     """Binary Tree implementation with comprehensive operations"""
#     def __init__(self):
#         self.root = None
#         self.size = 0
    
#     def is_empty(self):
#         """Check if tree is empty"""
#         return self.root is None

#     def get_size(self):
#         """Return number of nodes in tree"""
#         return self.size

#     def get_height(self,node=None):
#         """Calculate height of tree - O(n)"""
#         node = self.root
#         if node is None:
#             return -1
#         left_height = self.get_height(node.left)
#         right_height = self.get_height(node.right)
#         return 1 + max(left_height,right_height)
    
#     def depth_of_node(self,target,node= None,current_depth = 0):
#         """Find depth of a specific node"""
#         if node is None:
#             node = self.root
#         if node is None:
#             return -1
#         if node.data == target:
#             return current_depth
#         left_depth = self.depth_of_node(target,node.left,current_depth+1)
#         if left_depth != -1:
#             return left_depth
#         return self.depth_of_node(target,node.right,current_depth+1)
    
#     def count_nodes(self,node= None):
#         """Find depth of a specific node"""
#         if node is None:
#             node = self.root
#         if node is None:
#             return 0
#         return 1+ self.count_nodes(node.left) + self.count_nodes(node.right)
    
#     def count_leaf_nodes(self):
#         """Count leaf nodes (nodes with no children)"""        
#         if node is None:
#             node = self.root
#         if node is None:
#             return  0
#         if node.left is None and node.right is None:
#             return 1
#         return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
    
#     def is_balanced(self,node= None):
#         """Check if tree is height-balanced"""
#         def check_height(node):
#             if node is None:
#                 return 0 
#             left_height = check_height(node.left)
#             right_height = check_height(node.right)
#             if left_height == -1 or right_height == -1:
#                 return -1
#             if abs(left_height - right_height) > 1:
#                 return -1
#             return 1 + max(left_height,right_height)
#         if node is None:
#             node = self.root
#         return check_height(node) != -1

#     def insert_level_order(self,data):
#         """Insert node in level order (complete binary tree style) - O(n)"""
#         new_node = Node(data)
#         if self.root is None:
#             self.root = new_node
#             self.size += 1
#             print(f"Inserted root: {data}")
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
#             else:
#                 queue.append(current.left)
#                 queue.append(current.right)
# # ===============TREE TRAVERSAL - RECURSIVE ========================= #
#     def inorder_recursive(self,node = None):                            
#         """Inorder traversal: Left → Root → Right"""
#         if node is None:
#             node = self.root
#         result = []
#         if node:
#             result.extend(self.inorder_recursive(self.left))
#             result.append(node.data)
#             result.extend(self.inorder_recursive(self.right))
#         return result

#     def preorder_recursive(self,node = None):
#         """Preorder traversal: Root → Left → Right"""
#         if node is None:
#             node = self.root
#         result = []
#         if node:
#             result.append(node.data)
#             result.extend(self.preorder_recursive(self.left))
#             result.extend(self.preorder_recursive(self.right))
#         return result

#     def postorder_recursive(self,node = None):
#         """Postorder traversal: Left → Right → Root"""
#         if node is None:
#             node = self.root
#         result = []
#         if node:
#             result.extend(self.postorder_recursive(self.left))
#             result.extend(self.postorder_recursive(self.right))
#             result.append(node.data)
#         return result
# # ================================================================== #

# # ==================TREE TRAVERSAL - ITERATIVE ======================= #

#     def inorder_iterative(self,node= None):
#         """Inorder traversal using stack (iterative)"""
#         if not self.root:
#             return []
#         result = []
#         stack = []
#         current = self.root
#         while stack or current:
#             while current:
#                 stack.append(current)
#                 current = current.left
#         current = stack.pop()
#         result.append(current.data)
#         current = current.right

#         return result
#     def preorder_iterative(self,node= None):
#         """Preorder traversal: Root → Left → Right"""
#         if not self.root:
#             return []
#         result = []
#         stack = [self.root]
#         while stack:
#             node = stack.pop()
#             result.append(node.data)
#             if node.right:
#                 stack.append(node.data)
#             if node.left:
#                 stack.append(node.left)
#         return result

#     def level_order(self):
#         """Level order traversal (BFS) using queue"""
#         if not self.root:
#             return []
#         result = []
#         queue = deque([self.root])
#         while queue:
#             node = queue.popleft()
#             result.append(node.data)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         return result

#     def level_order_with_levels(self):
#         """Level order traversal returning nodes grouped by level"""
#         if not self.root:
#             return []
#         result = []
#         queue = deque([self.root])
#         while queue:
#             level_size = len(queue)
#             current_level = []
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 current_level.append(node.data)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             result.append(current_level)
#         return result


#     def search(self,target,node = None):
#         """Search for a value in the tree - O(n)"""
#         if node is None:
#             node  = self.root
#         if node is None:
#             return False
#         if node.data == target:
#             return True
#         return self.search(target,node.left) or self.search(target,node.right)

#     def display_tree(self):
#             """Display tree structure visually"""
#             if self.root is None:
#                 print("Tree is empty")
#                 return

#             print("Tree Structure:")
#             self._display_tree_helper(self.root, "", True)
#             print(f"Height: {self.height()}")
#             print(f"Total nodes: {self.get_size()}")
#             print(f"Leaf nodes: {self.count_leaf_nodes()}")
#             print(f"Is balanced: {self.is_balanced()}")
    
#     def _display_tree_helper(self, node, prefix, is_last):
#         """Helper method for tree visualization"""
#         if node is not None:
#             print(prefix + ("└── " if is_last else "├── ") + str(node.data))
            
#             children = [child for child in [node.left, node.right] if child]
            
#             for i, child in enumerate(children):
#                 is_last_child = i == len(children) - 1
#                 extension = "    " if is_last else "│   "
#                 self._display_tree_helper(child, prefix + extension, is_last_child)
class BinaryTree:
    """Binary Tree implementation with comprehensive operations"""
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def is_empty(self):
        """Check if tree is empty"""
        return self.root is None
    
    def get_size(self):
        """Return number of nodes in tree"""
        return self.size
    
    def insert_level_order(self, data):
        """Insert node in level order (complete binary tree style) - O(n)"""
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            self.size += 1
            print(f"Inserted root: {data}")
            return
        
        # Use queue for level order insertion
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
    
    # ============ TREE TRAVERSALS ============
    
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
        """Inorder traversal using stack (iterative)"""
        if not self.root:
            return []
        
        result = []
        stack = []
        current = self.root
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            result.append(current.data)
            
            # Move to right subtree
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
            
            # Push right first (so left is processed first)
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
        """Level order traversal (BFS) using queue"""
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
    
    # ============ TREE PROPERTIES ============
    
    def height(self, node=None):
        """Calculate height of tree - O(n)"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1  # Height of empty tree
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def depth_of_node(self, target, node=None, current_depth=0):
        """Find depth of a specific node"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1  # Node not found
        
        if node.data == target:
            return current_depth
        
        # Search in left subtree
        left_depth = self.depth_of_node(target, node.left, current_depth + 1)
        if left_depth != -1:
            return left_depth
        
        # Search in right subtree
        return self.depth_of_node(target, node.right, current_depth + 1)
    
    def count_nodes(self, node=None):
        """Count total number of nodes"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def count_leaf_nodes(self, node=None):
        """Count leaf nodes (nodes with no children)"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        # If it's a leaf node
        if node.left is None and node.right is None:
            return 1
        
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
    
    def is_balanced(self, node=None):
        """Check if tree is height-balanced"""
        def check_height(node):
            if node is None:
                return 0
            
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            
            # If subtree is unbalanced
            if left_height == -1 or right_height == -1:
                return -1
            
            # If current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        if node is None:
            node = self.root
        
        return check_height(node) != -1
    
    def search(self, target, node=None):
        """Search for a value in the tree - O(n)"""
        if node is None:
            node = self.root
        
        if node is None:
            return False
        
        if node.data == target:
            return True
        
        return self.search(target, node.left) or self.search(target, node.right)
    
    # ============ DISPLAY METHODS ============
    
    def display_tree(self):
        """Display tree structure visually"""
        if self.root is None:
            print("Tree is empty")
            return
        
        print("Tree Structure:")
        self._display_tree_helper(self.root, "", True)
        print(f"Height: {self.height()}")
        print(f"Total nodes: {self.get_size()}")
        print(f"Leaf nodes: {self.count_leaf_nodes()}")
        print(f"Is balanced: {self.is_balanced()}")
    
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
    print("=== Binary Tree Implementation ===\n")

    
    # Test Binary Tree
    print("1. Creating and populating Binary Tree:")
    bt = BinaryTree()
    
    # Insert nodes in level order
    for i in [1, 2, 3, 4, 5, 6, 7]:
        bt.insert_level_order(i)
    
    bt.display_tree()
    
    # Test traversals
    print("\n2. Tree Traversals:")
    print(f"Inorder (Recursive):   {bt.inorder_recursive()}")
    print(f"Inorder (Iterative):   {bt.inorder_iterative()}")
    print(f"Preorder (Recursive):  {bt.preorder_recursive()}")
    print(f"Preorder (Iterative):  {bt.preorder_iterative()}")
    print(f"Postorder (Recursive): {bt.postorder_recursive()}")
    print(f"Level Order:           {bt.level_order()}")
    print(f"Level Order by Levels: {bt.level_order_with_levels()}")
    
    # Test search and properties
    print("\n3. Tree Properties and Search:")
    print(f"Height: {bt.height()}")
    print(f"Search for 5: {bt.search(5)}")
    print(f"Search for 10: {bt.search(10)}")
    print(f"Depth of node 5: {bt.depth_of_node(5)}")
    print(f"Total nodes: {bt.count_nodes()}")
    print(f"Leaf nodes: {bt.count_leaf_nodes()}")
    print(f"Is balanced: {bt.is_balanced()}")
    