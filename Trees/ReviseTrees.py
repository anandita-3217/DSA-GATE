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

if __name__ == "__main__":
    print(f"Running Trees")