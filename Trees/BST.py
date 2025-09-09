from collections import deque


class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right 
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.root is None
    
    def get_size(self):
        return self.size
    
    def insert_bst(self,data):
        """Insert node maintaining BST property - O(log n) average, O(n) worst"""
        self.root = self.insert_bst_helper(self.root,data)
        self.size += 1
        print(f"Inserted {data} into BST")
    def insert_bst_helper(self,node,data):
        """Helper method for BST insertion"""
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self.insert_bst_helper(node.left,data)
        else: 
            node.right = self.insert_bst_helper(node.right,data)
        return node
    def inorder_recursive(self,node=None):
        """Inorder traversal: Left → Root → Right"""
        if self.root is None:
            raise ValueError("Empty ahh tree")
        if node is None:
            node = self.root
        result = []
        if node:
            result.extend(self.inorder_recursive(node.left))
            result.append(node.data)
            result.extend(self.inorder_recursive(node.right))
        return result
    def preorder_recursive(self,node= None):
        """Preorder traversal: Root → Left → Right"""
        if self.root is None:
            raise ValueError("Empty ahh tree")
        if node is None:
            node = self.root
        result = []
        if node:
            result.append(node.data)
            result.extend(self.preorder_recursive(node.left))
            result.extend(self.preorder_recursive(node.right))
        return result

    def postorder_recursive(self,node = None):
        """Postorder traversal: Left → Right → Root"""
        if self.root is None:
            raise ValueError("Empty ahh tree")
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
    def level_order_with_levels(self,node=None):
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
    def height(self, node=None):
        """Calculate height of tree - O(n)"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1  # Height of empty tree
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def depth_of_node(self,target,node=None,current_depth=0):
        """Find depth of a specific node"""
        if node is None:
            node = self.root
        if node is None:
            return -1
        if node.data == target:
            return current_depth
        left_depth = self.depth_of_node(target,node.left,current_depth+1)
        if left_depth != -1:
            return left_depth
        return self.depth_of_node(target,node.right,current_depth+1)

    def count_nodes(self,node = None):
        """Count total number of nodes"""
        if node is None:
            node = self.root
        if node is None:
            return 0 
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    def count_leaf_nodes(self,node= None):
        """Count total number of leaf nodes"""
        if node is None:
            node = self.root
        if node is None:
            return 0 
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
    def is_balanced(self,node=None):
        def check_height(node):
            if node is None:
                return 0
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height-right_height) > 1:
                return -1
            return 1+max(left_height,right_height)
        if node is None:
            node = self.root
        
        return check_height(node) != -1
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

    def search_bst(self,target):
        return self.search_helper(self.root,target)
    def search_helper(self,node,target):
        """Helper method for BST search"""
        if node is None:
            return False
        if node.data == target:
            return True
        if target<node.left:
            return self.search_helper(node.left,target)
        else:
            return self.search_helper(node.right,target)
    def find_min(self,node= None):
        """Find minimum value in BST"""
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.data
    def find_max(self,node=None):
        """Find maximum in BST"""
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.data
    def is_valid_bst(self,node= None, min_val= float('-inf'),max_val = float('inf')):
        """Check if tree satisfies BST property"""
        if node is None:
            node = self.root
        if node is None:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False
        return (self.is_valid_bst(node.left,min_val,node.data) and self.is_valid_bst(node.right,node.data,max_val))
    def delete_bst(self,data):
        """Delete node from BST maintaining BST property"""
        if self.search_bst(data):
            self.root = self.delete_bst_helper(self.root,data)
            self.size -= 1
            print(f"Deleted data from BST: {data}")
        else:
            print(f"Did not find data from BST: {data}")

    def delete_bst_helper(self,node,data):
        """Helper method for BST deletion"""
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete_bst_helper(node.left,data)
        elif data > node.data:
            node.right = self.delete_bst_helper(node.right,data)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor_data = self.find_min(node.right)
            node.data = successor_data
            node.right = self.delete_bst_helper(node.right,successor_data)
        return node

if __name__ == "__main__":
    bst = BST()
    for i in [1,2,3,4,5,6,7]:
        bst.insert_bst(i)
    bst.display_tree()
    print("\nTreeTraversal")
    print(f"Inorder: {bst.inorder_recursive()}")
    print(f"Preorder: {bst.preorder_recursive()}")
    print(f"Postorder: {bst.postorder_recursive()}")
    print(f"Level Order: {bst.level_order}")
    print(f"Level Order By Levels: {bst.level_order_with_levels}")
    print(f"Height: {bst.height}")
    print(f"Search for 5: {bst.search_bst(5)}")
    print(f"Search for 50: {bst.search_bst(50)}")
    print(f"Depth of node 5: {bst.depth_of_node(5)}")
    print(f"Total nodes: {bst.count_nodes}")
    print(f"Total Leaf nodes: {bst.count_leaf_nodes}")
    print(f"Is balanced: {bst.is_balanced()}")
    print(f"Minimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    print(f"Before deletion: {bst.inorder_recursive()}")
    
    # Delete leaf node
    bst.delete_bst(2)
    print(f"After deleting 2: {bst.inorder_recursive()}")
    
    # Delete node with one child
    bst.delete_bst(3)
    print(f"After deleting 3: {bst.inorder_recursive()}")
    
    # Delete node with two children
    bst.delete_bst(5)
    print(f"After deleting 5: {bst.inorder_recursive()}")
    
    bst.display_tree()