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

class TreeBst:
    def __init__(self, root=None):
        self.root = root
        
    def search(self, data):
        root = self.root
        
        while root and root.data != data:
            if root.data > data:
                root = root.left_child
            else:
                root = root.right_child
        
        return root
    
        ''' use recursive
        def search_recursive(root):
            if root is None:
                return None
            
            if root.data == data:
                return root
            
            if root.data > data:
                return search_recursive(root.left_child)
            else:
                return search_recursive(root.right_child) 
        
        return search_recursive(self.root)'''
    
    def insert_iterative(self, data):
        node = TreeNode(data)
        root = self.root
        parent = None
        
        while root and data != root.data:
            parent = root
            if root.data > data:
                root = root.left_child
            else:
                root = root.right_child
        
        if not parent:
            self.root = node
            return
        
        if parent.data > data:
            parent.left_child = node
        else:
            parent.right_child = node
    
    def insert(self, data):
        parent = None
        def insert_recursive(root):
            nonlocal parent
            if root is None:
                if parent:
                    if parent.data > data:
                        parent.left_child = TreeNode(data)
                    else:
                        parent.right_child = TreeNode(data)
                    return self.root
                
                return TreeNode(data)
            
            parent = root
            
            if root.data > data:
                return insert_recursive(root.left_child)
            else:
                return insert_recursive(root.right_child)
            
        self.root = insert_recursive(self.root)

    def delete(self, data):
        parent = None
        def delete_recursive(root):
            nonlocal parent
            if root is None:
                return self.root
            
            if root.data == data:
                if not root.left_child and not root.right_child:
                    if parent.data > data:
                        parent.left_child = None
                    else:
                        parent.right_child = None
                    return self.root
                
                if not root.right_child:
                    root.data = root.left_child.data
                    root.left_child = None
                    return self.root
                
                if not root.left_child:
                    root.data = root.right_child.data
                    root.right_child = None
                    return self.root
                
                sub_root = root.left_child
                sub_parent = root
                
                while sub_root.right_child:
                    sub_parent = sub_root
                    sub_root = sub_root.right_child
                
                root.data = sub_root.data
                
                if sub_parent is root:
                    sub_parent.left_child = sub_root.left_child
                else:
                    sub_parent.right_child = sub_root.left_child
                
                return self.root
            
            parent = root
            
            if root.data > data:
                return delete_recursive(root.left_child)
            else:
                return delete_recursive(root.right_child)
        
        self.root = delete_recursive(self.root)
    
    def traverse_inorder(self):
        ret = []
        def inorder_recursive(root):
            if not root:
                return
            
            inorder_recursive(root.left_child)
            ret.append(root)
            inorder_recursive(root.right_child)

        inorder_recursive(self.root)
        return ret


if __name__ == "__main__":
    tree = TreeBst()
    elems = 30, 5, 40, 2, 80, 35
    for i in elems:
        tree.insert(i)
        
    actions = tree.traverse_inorder()
    print(actions)
    
    tree.delete(80)
    actions = tree.traverse_inorder()
    print(actions)
    
    '''sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    
    root = TreeBinaryBuilder.build(sexpr)
    assert root
    
    tree = TreeBst(root)
    
    found = tree.search(5)
    print(found)
    found = tree.search(2)
    print(found)
    found = tree.search(40)
    print(found)
    found = tree.search(30)
    print(found)
    found = tree.search(35)
    print(found)'''