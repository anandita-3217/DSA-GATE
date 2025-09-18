from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
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
    def insert_level_order(self,data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            self.size += 1
            print(f"new_node is the new_node root: {data}")
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
                print(f"Inserted{data} as right child of {current.data}")
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def inorder_recursive(self,node = None):
        if node is None:
            node=self.root
        result =[]
        if node:
            result.extend(self.inorder_recursive(node.left))
            result.append(node.data)
            result.extend(self.inorder_recursive(node.right))
        return  result
    
    def inorder_iterative(self,node=None):
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
    
    def preorder_traversal(self,node=None):
        if node is None:
            node = self.root
        result =  []
        if node:
            result.append(node.data)
            result.extend(self.preorder_traversal(node.left))
            result.extend(self.preorder_traversal(node.right))

        return  result
    
    def preorder_iterative(self):
        if not self.root:
            return  []
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return  result
    def postorder_traversal(self,node=None):
        if node is None:
            node = self.root
        result = []
        if node:
            result.extend(self.postorder_traversal(node.left))
            result.extend(self.postorder_traversal(node.right))
            result.append(node.data)
        return result

    def level_order(self):
        if not self.root:
            return  []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return  result
    def level_order_with_levels(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
    def count_nodes(self,node= None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1+self.count_leaf_nodes(node.left)+self.count_nodes(node.right)
    def count_leaf_nodes(self,node = None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) +self.count_nodes(node.right)
    def height(self,node=None):
        if node is None:
            node = self.root
        if node is None:
            return  -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height,right_height)

    def display_tree(self):
        if self.root is None:
            return
        print("Tree Structure: ")
        self._display_tree_helper(self.root,"",True)
        print(f"Total Node: {self.get_size()}")
        print(f"Height: {self.height()}")


    def _display_tree_helper(self,node,prefix,is_last):
        if node is None:
            node = self.root
            children = [child for child in [node.left,node.right] if child]
            for i, child in enumerate(children):
                is_last_child = i == len(children) - 1
                extension = "   " if is_last else "|    "
                self._display_tree_helper(child,prefix+extension,is_last_child)
if __name__ == "__main__":
    print(f"Running Trees")
    print("1. Creating Binary Tree")
    bt = BinaryTree()
    for i in [1,2,3,4,5,6,7]:
        bt.insert_level_order(i)
    print("\n2. Tree Traversals:")
    print(f"Inorder (Recursive):   {bt.inorder_recursive()}")
    print(f"Inorder (Iterative):   {bt.inorder_iterative()}")
    print(f"Preorder (Recursive):  {bt.preorder_traversal()}")
    print(f"Preorder (Iterative):  {bt.preorder_iterative()}")
    print(f"Postorder (Recursive): {bt.postorder_traversal()}")
    print(f"Level Order:           {bt.level_order()}")
    print(f"Level Order by Levels: {bt.level_order_with_levels()}")
