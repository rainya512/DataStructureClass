class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __repr__(self):
        return f"{self}"
    
    def __str__(self):
        return f"{self.data}"

class TreeBinaryBuilder:
    @staticmethod
    def build(sexpr):
        stack = []
        add = lambda node: node if node.data != "#" else None
        
        root = None
        for tok in sexpr:
            if tok != ")":
                stack.append(TreeNode(tok))
                continue
            root_ = None
            while stack[-1].data != "(":
                node = stack.pop()
                if root_ is None:
                    root_ = node
                    continue
                right, root_ = root_, TreeNode(None)
                root_.left_child, root_.right_child = add(node), add(right)
            stack.pop()
                
            if not stack:
                return root_
            
            assert root_
            root = stack.pop()
            root_.data = root.data
            stack.append(root_)
        
        return root

class TreeBinary:
    def __init__(self, root):
        self.root = root
    
    def dfs(self, data):
        stack = []
        
        root = self.root
        
        while root or stack:
            while root:
                if root.data == data:
                    return root
                stack.append(root.right_child)
                root = root.left_child
            root = stack.pop()
        
        return root

    def bfs(self, data):
        queue = []
        queue.append(self.root)
        
        while queue:
            root = queue.pop(0)
            if root.data == data:
                return root
            if root.left_child:
                queue.append(root.left_child)
            if root.right_child:
                queue.append(root.right_child)
        
        return

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    
    root = TreeBinaryBuilder.build(sexpr)
    tree = TreeBinary(root)
    assert root
    
    for e in sexpr:
        node = tree.bfs(e)
        print("target:", e, " found:", node)