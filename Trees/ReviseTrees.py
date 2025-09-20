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
#     def insert_level_order(self,data):
#         new_node = TreeNode(data)
#         if self.root is None:
#             self.root = new_node
#             self.size += 1
#             print(f"new_node is the new_node root: {data}")
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
#                 print(f"Inserted{data} as right child of {current.data}")
#                 return
#             else:
#                 queue.append(current.left)
#                 queue.append(current.right)

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
    
#     def inorder_iterative(self):
#         """Inorder traversal using stack (iterative)"""
#         if not self.root:
#             return []
        
#         result = []
#         stack = []
#         current = self.root
        
#         while stack or current:
#             # Go to leftmost node
#             while current:
#                 stack.append(current)
#                 current = current.left
            
#             # Process current node
#             current = stack.pop()
#             result.append(current.data)
            
#             # Move to right subtree
#             current = current.right
        
#         return result
    
#     def preorder_recursive(self, node=None):
#         """Preorder traversal: Root → Left → Right"""
#         if node is None:
#             node = self.root
        
#         result = []
#         if node:
#             result.append(node.data)
#             result.extend(self.preorder_recursive(node.left))
#             result.extend(self.preorder_recursive(node.right))
        
#         return result
    
#     def preorder_iterative(self):
#         """Preorder traversal using stack (iterative)"""
#         if not self.root:
#             return []
        
#         result = []
#         stack = [self.root]
        
#         while stack:
#             node = stack.pop()
#             result.append(node.data)
            
#             # Push right first (so left is processed first)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return result
    
#     def postorder_recursive(self, node=None):
#         """Postorder traversal: Left → Right → Root"""
#         if node is None:
#             node = self.root
        
#         result = []
#         if node:
#             result.extend(self.postorder_recursive(node.left))
#             result.extend(self.postorder_recursive(node.right))
#             result.append(node.data)
        
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
    
#     def count_nodes(self,node= None):
#         if node is None:
#             node = self.root
#         if node is None:
#             return 0
#         return 1+self.count_nodes(node.left)+self.count_nodes(node.right)

#     def count_leaf_nodes(self, node=None):
#         """Count leaf nodes (nodes with no children)"""
#         if node is None:
#             node = self.root
        
#         if node is None:
#             return 0
        
#         # If it's a leaf node
#         if node.left is None and node.right is None:
#             return 1
        
#         return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
#     def is_balanced(self, node=None):
#         """Check if tree is height-balanced"""
#         def check_height(node):
#             if node is None:
#                 return 0
            
#             left_height = check_height(node.left)
#             right_height = check_height(node.right)
            
#             # If subtree is unbalanced
#             if left_height == -1 or right_height == -1:
#                 return -1
            
#             # If current node is unbalanced
#             if abs(left_height - right_height) > 1:
#                 return -1
            
#             return 1 + max(left_height, right_height)
        
#         if node is None:
#             node = self.root
        
#         return check_height(node) != -1
    
    
#     def height(self, node=None):
#         """Calculate height of tree - O(n)"""
#         if node is None:
#             node = self.root
        
#         if node is None:
#             return -1  # Height of empty tree
        
#         left_height = self.height(node.left)
#         right_height = self.height(node.right)
        
#         return 1 + max(left_height, right_height)
#     def display_tree(self):
#         """Display tree structure visually"""
#         if self.root is None:
#             print("Tree is empty")
#             return
        
#         print("Tree Structure:")
#         self._display_tree_helper(self.root, "", True)
#         # print(f"Height: {self.height()}")
#         print(f"Total nodes: {self.get_size()}")
#         print(f"Leaf nodes: {self.count_leaf_nodes()}")
#         print(f"Is balanced: {self.is_balanced()}")
    
#     def _display_tree_helper(self, node, prefix, is_last):
#         """Helper method for tree visualization"""
#         if node is not None:
#             print(prefix + ("└── " if is_last else "├── ") + str(node.data))
            
#             children = [child for child in [node.left, node.right] if child]
            
#             for i, child in enumerate(children):
#                 is_last_child = i == len(children) - 1
#                 extension = "    " if is_last else "│   "
#                 self._display_tree_helper(child, prefix + extension, is_last_child)

# class BinarySearchTree(BinaryTree):
#     def __init__(self):
#         super().__init__()
    
#     def insert_bst(self,data):
#         self.root = self._insert_bst_helper(self.root,data)
#         self.size += 1
#         print(f"Inserted {data}")
#     def _insert_bst_helper(self,node,data):
#         if node is None:
#             return TreeNode(data)
        
#         if data < node.data:
#             node.left = self._insert_bst_helper(node.left,data)
#         else:
#             node.right = self._insert_bst_helper(node.right,data)
#         return node
#     def search_bst(self,target):
#         return self._search_helper(self.root,target)
#     def _search_helper(self,node, target):
#         if node is None:
#             return False
#         if node.data == target:
#             return True
#         elif target < node.data:
#             return self._search_helper(node.left,target)
#         else:
#             return self._search_helper(node.right,target)
# if __name__ == "__main__":
#     print("=== Binary Tree Implementation ===\n")
    
#     # Test Binary Tree
#     print("1. Creating and populating Binary Tree:")
#     bt = BinaryTree()
    
#     # Insert nodes in level order
#     for i in [1, 2, 3, 4, 5, 6, 7]:
#         bt.insert_level_order(i)
    
#     bt.display_tree()
    
#     # Test traversals
#     print("\n2. Tree Traversals:")
#     # print(f"Inorder (Iterative):   {bt.inorder_iterative()}")
#     # print(f"Preorder (Iterative):  {bt.preorder_iterative()}")
#     # print(f"Level Order:           {bt.level_order()}")
#     # print(f"Level Order by Levels: {bt.level_order_with_levels()}")

#     # print(f"Preorder (Recursive):  {bt.preorder_recursive()}")
#     # print(f"Inorder (Recursive):   {bt.inorder_recursive()}")
#     # print(f"Postorder (Recursive): {bt.postorder_recursive()}")
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
        new_node = TreeNode(data)
        
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

class BinarySearchTree(BinaryTree):
    """Binary Search Tree implementation extending BinaryTree"""
    
    def __init__(self):
        super().__init__()
    
    def insert_bst(self, data):
        """Insert node maintaining BST property - O(log n) average, O(n) worst"""
        self.root = self._insert_bst_helper(self.root, data)
        self.size += 1
        print(f"Inserted {data} into BST")
    
    def _insert_bst_helper(self, node, data):
        """Helper method for BST insertion"""
        if node is None:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_bst_helper(node.left, data)
        else:
            node.right = self._insert_bst_helper(node.right, data)
        
        return node
    
    def search_bst(self, target):
        """Search in BST - O(log n) average, O(n) worst"""
        return self._search_bst_helper(self.root, target)
    
    def _search_bst_helper(self, node, target):
        """Helper method for BST search"""
        if node is None:
            return False
        
        if node.data == target:
            return True
        elif target < node.data:
            return self._search_bst_helper(node.left, target)
        else:
            return self._search_bst_helper(node.right, target)
    
    def find_min(self, node=None):
        """Find minimum value in BST"""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        while node.left:
            node = node.left
        
        return node.data
    
    def find_max(self, node=None):
        """Find maximum value in BST"""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        while node.right:
            node = node.right
        
        return node.data
    
    def delete_bst(self, data):
        """Delete node from BST maintaining BST property"""
        if self.search_bst(data):
            self.root = self._delete_bst_helper(self.root, data)
            self.size -= 1
            print(f"Deleted {data} from BST")
        else:
            print(f"{data} not found in BST")
    
    def _delete_bst_helper(self, node, data):
        """Helper method for BST deletion"""
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_bst_helper(node.left, data)
        elif data > node.data:
            node.right = self._delete_bst_helper(node.right, data)
        else:
            # Node to delete found!
            
            # Case 1: No children (leaf node)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Two children - find inorder successor
            successor_data = self.find_min(node.right)
            node.data = successor_data
            node.right = self._delete_bst_helper(node.right, successor_data)
        
        return node
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """Check if tree satisfies BST property"""
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.data) and
                self.is_valid_bst(node.right, node.data, max_val))

class TreeApplications:
    """Common tree applications for GATE preparation"""
    
    @staticmethod
    def expression_tree_evaluation():
        """Example of expression tree evaluation"""
        # Create expression tree for: (3 + 5) * (2 - 1)
        root = TreeNode('*')
        root.left = TreeNode('+')
        root.right = TreeNode('-')
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(1)
        
        def evaluate_expression_tree(node):
            if node is None:
                return 0
            
            # If leaf node, return the value
            if node.left is None and node.right is None:
                return node.data
            
            # Evaluate left and right subtrees
            left_val = evaluate_expression_tree(node.left)
            right_val = evaluate_expression_tree(node.right)
            
            # Apply the operator
            if node.data == '+':
                return left_val + right_val
            elif node.data == '-':
                return left_val - right_val
            elif node.data == '*':
                return left_val * right_val
            elif node.data == '/':
                return left_val / right_val
        
        return evaluate_expression_tree(root)
    
    @staticmethod
    def lowest_common_ancestor(root, p, q):
        """Find Lowest Common Ancestor of two nodes"""
        if root is None:
            return None
        
        # If both p and q are present in left subtree
        if root.data > p and root.data > q:
            return TreeApplications.lowest_common_ancestor(root.left, p, q)
        
        # If both p and q are present in right subtree
        if root.data < p and root.data < q:
            return TreeApplications.lowest_common_ancestor(root.right, p, q)
        
        # If we reach here, root is the LCA
        return root.data
    
    @staticmethod
    def path_sum(root, target_sum):
        """Check if there exists a root-to-leaf path with given sum"""
        def has_path_sum(node, remaining_sum):
            if node is None:
                return False
            
            remaining_sum -= node.data
            
            # If it's a leaf node
            if node.left is None and node.right is None:
                return remaining_sum == 0
            
            # Check left or right subtree
            return (has_path_sum(node.left, remaining_sum) or
                   has_path_sum(node.right, remaining_sum))
        
        return has_path_sum(root, target_sum)

# Example usage and comprehensive testing
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
    
    # Test Binary Search Tree
    print("\n4. Binary Search Tree Operations:")
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert_bst(val)
    
    bst.display_tree()
    
    print(f"\nInorder traversal (should be sorted): {bst.inorder_recursive()}")
    
    # Test BST operations
    print(f"\nBST Search for 40: {bst.search_bst(40)}")
    print(f"BST Search for 100: {bst.search_bst(100)}")
    print(f"Minimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    # Test deletion
    print(f"\n5. BST Deletion:")
    print(f"Before deletion: {bst.inorder_recursive()}")
    
    # Delete leaf node
    bst.delete_bst(20)
    print(f"After deleting 20: {bst.inorder_recursive()}")
    
    # Delete node with one child
    bst.delete_bst(30)
    print(f"After deleting 30: {bst.inorder_recursive()}")
    
    # Delete node with two children
    bst.delete_bst(50)
    print(f"After deleting 50: {bst.inorder_recursive()}")
    
    bst.display_tree()
    
    # Test tree applications
    print("\n6. Tree Applications:")
    
    # Expression tree evaluation
    result = TreeApplications.expression_tree_evaluation()
    print(f"Expression tree (3+5)*(2-1) evaluates to: {result}")
    
    # Create BST for LCA testing
    lca_bst = BinarySearchTree()
    for val in [20, 10, 30, 5, 15, 25, 35]:
        lca_bst.insert_bst(val)
    
    lca = TreeApplications.lowest_common_ancestor(lca_bst.root, 5, 15)
    print(f"LCA of 5 and 15: {lca}")
    
    # Path sum testing
    has_path = TreeApplications.path_sum(lca_bst.root, 35)  # 20 + 10 + 5
    print(f"Path sum 35 exists: {has_path}")
    
    # Error handling
    print("\n7. Error Handling:")
    empty_tree = BinaryTree()
    print(f"Empty tree height: {empty_tree.height()}")
    print(f"Empty tree inorder: {empty_tree.inorder_recursive()}")
    
    print("\n=== Tree Implementation Complete ===")
    
    # GATE-style complexity summary
    print("\n=== GATE Complexity Summary ===")
    print("Binary Tree Operations:")
    print("- Search: O(n)")
    print("- Insertion (level order): O(n)")
    print("- Traversals: O(n)")
    print("- Height calculation: O(n)")
    print()
    print("Binary Search Tree Operations:")
    print("- Search: O(log n) average, O(n) worst")
    print("- Insert: O(log n) average, O(n) worst")  
    print("- Delete: O(log n) average, O(n) worst")
    print("- Inorder traversal: Always gives sorted output")
    print()
    print("Memory: O(n) for n nodes")
    print("Height: O(log n) for balanced, O(n) for skewed")