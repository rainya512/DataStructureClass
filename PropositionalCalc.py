class TreeNode:
    def __init__(self, data):
        self.data = data
        self.value = None # boolean value
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

class Treebinary:
    def __init__(self, root):
        self.root = root
    
    def calculate_propositional(self, *param):
        def calculate_recursive(root):
            if not root:
                return
            
            calculate_recursive(root.left_child)
            calculate_recursive(root.right_child)
            
            if root.data.isdigit():
                root.value = param[int(root.data)]
            elif root.data == "AND":
                root.value = root.left_child.value and root.right_child.value
            elif root.data == "OR":
                root.value = root.left_child.value or root.right_child.value
            elif root.data == "NOT":
                root.value = not root.right_child.value
            
            if root == self.root:
                return root
        
        ret = calculate_recursive(self.root)
        return ret

if __name__ == "__main__":
    sexpr = "( OR ( OR ( AND ( 0 NOT ( # 1 ) ) AND ( NOT ( # 0 ) 2 ) ) NOT ( # 2 ) ) )".split()
    root = TreeBinaryBuilder.build(sexpr)
    assert root
    
    tree = Treebinary(root)
    prop = tree.calculate_propositional(False, True, False)
    assert prop
    print(prop.value)

