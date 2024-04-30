class Tree:
    def __init__(self):
        self.root = None
    
    def build(self, sexpr):
        stack = []
        parent = None
        
        for e in sexpr:
            if e == ")":
                while stack[-1] != "(":
                    stack.pop()
                stack.pop()
            
            else:
                if e.isalpha():
                    new = Tree.TreeNode(e)
                    
                    if stack[-1] == "(":
                        if self.root is None:
                            self.root = new
                            parent = self.root
                            stack.append(e)
                            continue
                        
                        parent.left_child = new
                    else:
                        parent.right_sibling = new
                    
                    parent = new
                
                stack.append(e)
    
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_sibling = None
        
        def __str__(self):
            return f"{self.data}"

if __name__ == "__main__":
    expr = "( A ( B ( E ( K L "
    tree = Tree()
    tree.build(expr.split())
    
    a = tree.root
    print(a)
    
    assert a
    b = a.left_child
    print(b)
    
    
    e = b.left_child
    print(e)
    
    
    k = e.left_child
    print(k)
    l = k.right_sibling
    print(l)