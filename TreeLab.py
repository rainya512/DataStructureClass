class Tree:
    def __init__(self):
        self.root = None
    
    def build(self, sexpr):
        stack = []
        nexpr = ""
        
        # change sexpr into postfix form
        for e in sexpr:
            if e == ")":
                while stack[-1] != "(":
                    nexpr += stack.pop()
                nexpr += stack.pop()
            
            else:
                # sibling sign
                if e.isalpha():
                    if literal.isalpha():
                        stack.append("+")
                    
                    nexpr += e
                else:
                    stack.append(e)
                
                literal = e
        
        while len(stack) > 0:
            nexpr += stack.pop()
        
        # logic for build tree (use postfix calculation)
        for e in nexpr:
            if e.isalpha():
                stack.append(Tree.TreeNode(e))
            else:
                if len(stack) <= 1:
                    self.root = stack.pop()
                    break
                
                c = stack.pop()
                p = stack.pop()
                
                if e == "+":
                    p.right_sibling = c
                elif e == "(":
                    p.left_child = c
                
                stack.append(p)

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_sibling = None
        
        def __str__(self):
            return f"{self.data}"

if __name__ == "__main__":
    expr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    tree = Tree()
    tree.build(expr.split())
    
    a = tree.root
    print(a)
    
    assert a
    b = a.left_child
    print(b)
    c = b.right_sibling
    print(c)
    d = c.right_sibling
    print(d)
    
    e = b.left_child
    print(e)
    f = e.right_sibling
    print(f)
    
    g = c.left_child
    print(g)
    
    h = d.left_child
    print(h)
    i = h.right_sibling
    print(i)
    j = i.right_sibling
    print(j)
    
    k = e.left_child
    print(k)
    l = k.right_sibling
    print(l)
    
    m = h.left_child
    print(m)
