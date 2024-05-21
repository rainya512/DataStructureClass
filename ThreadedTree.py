class TreeNodeThreaded:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.left_thread = False
        self.right_thread = False
    
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
                stack.append(TreeNodeThreaded(tok))
                continue
            root_ = None
            while stack[-1].data != "(":
                node = stack.pop()
                if root_ is None:
                    root_ = node
                    continue
                right, root_ = root_, TreeNodeThreaded(None)
                root_.left_child, root_.right_child = add(node), add(right)
            stack.pop()
                
            if not stack:
                return root_
            
            assert root_
            root = stack.pop()
            root_.data = root.data
            stack.append(root_)
        
        return root

class TreeBinaryThreadedBuilder:
    @staticmethod
    def build(root):
        head = TreeNodeThreaded()
        head.left_child, head.right_child = root, head
        pred = head
        
        def inorder_recursive(root):
            nonlocal pred
            if root is None:
                return

            inorder_recursive(root.left_child)
            if not root.left_child:
                root.left_thread = True
                root.left_child = pred
            
            if not pred.right_child:
                pred.right_thread = True
                pred.right_child = root
            
            pred = root
            inorder_recursive(root.right_child)
        
        inorder_recursive(root)
        
        pred.right_thread = True
        pred.right_child = head
        return head

class TreeBianryThread:
    def __init__(self, head):
        self.head = head
    
    def find_successor(self, root):
        node = root.right_child
        if not root.right_thread:
            while node and not node.left_thread:
                node = node.left_child
        
        return node
    
    def traverse_inorder(self):
        ret = []
        root = self.find_successor(self.head)
        
        while root and root is not self.head:
            ret.append(root)
            root = self.find_successor(root)
        
        return ret

    def traverse_preorder(self):
        ret = []
        root = self.head.left_child
            
        while root and root is not self.head:
            ret.append(root)
            if not root.left_thread:
                root = root.left_child
            else:
                while root and root.right_thread:
                    root = root.right_child
                
                if root:
                    root = root.right_child
                
        return ret

    def traverse_postorder(self):
        ret = []
        root = self.find_successor(self.head)
        parent = None

        while root is not self.head.left_child and root is not self.head:
            while not root.left_thread and not root.right_thread :
                parent = root
                root = self.find_successor(root)
            
            ret.append(root)
            root = self.find_successor(root)
            
            if parent:
                ret.append(parent)
        
        root = self.find_successor(root)
        parent = None
        
        while root is not self.head.left_child and root is not self.head:
            while not root.left_thread and not root.right_thread:
                parent = root
                root = self.find_successor(root)
            
            ret.append(root)
            root = self.find_successor(root)
            
            if parent:
                ret.append(parent)
        
        ret.append(root.left_child)
        return ret

if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    root = TreeBinaryBuilder.build(sexpr)
    assert root
    
    head = TreeBinaryThreadedBuilder.build(root)
    assert head
    
    tree = TreeBianryThread(head)
    actions = tree.traverse_inorder()
    print(actions)
    
    actions = tree.traverse_preorder()
    print(actions)
    
    actions = tree.traverse_postorder()
    print(actions)