class TreeBinary:
    def __init__(self, root):
        self.root = root
    
    def traverse_inorder(self):
        ret = []
        stack = []
        
        root = self.root
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left_child
            
            if root is None:
                root = stack.pop()
                ret.append(root)
                root = root.right_child
        
        '''
        # use recursive
        
        def inorder_recursive(root):
            if not root:
                return
            
            inorder_recursive(root.left_child)
            ret.append(root)
            inorder_recursive(root.right_child)
        
        inorder_recursive(self.root)
        '''
        return ret
    
    def traverse_preorder(self):
        ret = []
        stack = []
        
        root = self.root
        stack.append(root)
        
        while len(stack) != 0:
            root = stack.pop()
            ret.append(root)
            
            if root.right_child is not None:
                stack.append(root.right_child)
            if root.left_child is not None:
                stack.append(root.left_child)
        
        '''
        # use recursive
        def preorder_recursive(root):
            if not root:
                return
            
            ret.append(root)
            preorder_recursive(root.left_child)
            preorder_recursive(root.right_child)
    
        preorder_recursive(self.root)
        '''
        return ret
    
    def traverse_postorder(self):
        ret = []
        stack = []
        
        root = self.root
        stack.append(root)
        
        while len(stack) != 0:
            root = stack.pop()
            ret.append(root)
            
            if root.left_child is not None:
                stack.append(root.left_child)
            if root.right_child is not None:
                stack.append(root.right_child)
        
        ret.reverse()
        
        '''
        # use recursive
        def postorder_recursive(root):
            if not root:
                return
            
            postorder_recursive(root.left_child)
            postorder_recursive(root.right_child)
            ret.append(root)
    
        postorder_recursive(self.root)
        '''
        return ret

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

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = TreeBinaryBuilder.build(sexpr)
    assert root
    
    tree = TreeBinary(root)
    actions = tree.traverse_inorder()
    print(actions)
    actions = tree.traverse_preorder()
    print(actions)
    actions = tree.traverse_postorder()
    print(actions)