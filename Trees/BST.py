class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right 
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        super().__init__()