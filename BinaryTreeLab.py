class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        
        self.left_child = None
        self.right_child = None
    
    def __str__(self):
        return f"{self.data}"

class TreeBinary:
    def __init__(self) -> None:
        self.root = None
    
    def build(self, sexpr):
        stack = []
        nexpr = []
        
        for e in sexpr:
            if e == ")":
                while stack[-1] != "(":
                    nexpr.append(stack.pop())
                nexpr.append(stack.pop())
            
            else:
                # sibling sign
                if e == "#" or e.isdecimal():
                    if literal == "#" or literal.isdecimal():
                        stack.append("+")
                    
                    nexpr.append(e)
                else:
                    stack.append(e)
                
                literal = e
        
        while len(stack) > 0:
            nexpr.append(stack.pop())
        
        # logic for build tree (use postfix calculation)
        for e in nexpr:
            if e.isdecimal():
                stack.append(TreeNode(e))
            elif e == "#":
                stack.append(None)
            else:
                if len(stack) <= 1:
                    break
                
                if e == "+":
                    right = stack.pop()
                    left = stack.pop()

                    stack[-1].left_child = left
                    stack[-1].right_child = right
                    
                elif e == "(":
                    child = stack.pop()
                    parent = stack[-1]
                    
                    if parent.left_child is None:
                        parent.left_child = child
                    else:
                        parent.right_child = child
            
        self.root = stack.pop()

if __name__ == "__main__" :
    sexpr = "( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )".split()
    
    tree = TreeBinary()
    tree.build(sexpr)
    
    root = tree.root
    print(root)
    print(root.left_child)
    print(root.left_child.left_child)
    print(root.left_child.right_child)
    print(root.right_child)
    print(root.right_child.left_child)
    print(root.right_child.right_child)