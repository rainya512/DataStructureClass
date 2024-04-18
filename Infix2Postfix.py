class Stack:
    def __init__(self, capacity=5) -> None:
        self.capacity = capacity
        self.arr = [None] * capacity
        
        self.top = -1
    
    def empty(self):
        return self.top == -1
    
    def full(self):
        return self.top >= self.capacity - 1
    
    def size(self):
        return self.top + 1
    
    def push(self, item):
        if self.full():
            raise IndexError("push from full stack")
        
        self.top += 1
        self.arr[self.top] = item
    
    def peek(self):
        if self.empty():
            raise IndexError("peek from empty stack")
        
        return self.arr[self.top]
    
    def pop(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        
        res = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        
        return res
    
    def __str__(self):
        res = []
        i = 0
        while i < self.size():
            res.append(self.arr[i])
            i += 1
        
        res = ", ".join(map(str, res))
        return f"[{res}]"

def infix_to_postfix(expr):
    OPS = {"+", "-", "*", "/", "^", "(", ")"}
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, None: -9}
    
    res = ""
    stack = Stack(len(expr))
    
    for token in expr:
        if token not in OPS:
            res += token
            continue
        
        if stack.empty() or token == "(" or stack.peek() == "(":
            stack.push(token)
        elif token == ")":
            while(stack.peek() != "("):
                res += str(stack.pop())
            stack.pop()
        else:
            while(not stack.empty() and stack.peek() != "(" and prec[token] <= prec[stack.peek()]):
                res += str(stack.pop())
            
            stack.push(token)
    
    while(not stack.empty()):
        res += str(stack.pop())
    
    return "".join(res)

if __name__ == "__main__":
    expr = "a*(b+c)*d"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    
    expr = "a*b+c*d"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    
    expr = "a+b*c"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    
    expr = "a*b+c"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    
    expr = "a*(b+c)*d"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    
    expr = "a+(b*c+d)*e"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")