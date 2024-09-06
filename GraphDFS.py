from typing import Optional

def read_input(name_file="input.dat"):
    mat = []
    with open(name_file) as f:
        for line in f:
            (*row, ) = map(int, line.split())
            mat.append(row)
    return mat

def print_mat(mat):
    rows, cols = len(mat), len(mat[0])
    
    for row in range(rows):
        for col in range(cols):
            print(f"{mat[row][col]:2d}", end=" ")
        print("\b")

class Node:
    def __init__(self, data):
        self.data = data
        self.link: Optional[Node] = None
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.data}"

class Graph:
    def __init__(self, mat):
        self.mat = mat
        self.size = len(mat)
        self.heads = [Node(i) for i in range(self.size)]
        self.__build()
        
    def __build(self):
        for row in range(self.size):
            vt = self.heads[row]
            for col in range(self.size):
                if self.mat[row][col] == 1:
                    vt.link = Node(col)
                    vt = vt.link
    
    def dfs_recr(self, src, node, marked, ret):
        marked[src] = True
        
        while node:
            if not marked[node.data]:
                ret.append((src, node.data))
                self.dfs_recr(node.data, self[node.data], marked, ret)
            node = node.link
    
    def dfs_iter(self, node, marked, ret):
        stack = []
        stack.append(node)
        src = node.data
        
        while len(stack) != 0:
            marked[src] = True
            
            if node.link is None:
                node = stack.pop()
                src = node.data
            
            elif not marked[node.link.data]:
                ret.append((src, node.link.data))
                src = node.link.data
                node = self[src]
                stack.append(node)
            
            elif node:
                node = node.link
    
    def dfs(self, bgn):
        ret = []
        marked = [False] * self.size
        node = self[bgn]
        self.dfs_recr(bgn, node, marked, ret)
        #self.dfs_iter(node, marked, ret)
        return ret
    
    def bfs_iter(self, v):
        ret = []
        marked = [False] * self.size
        
        node = self[v]
        queue = []
        queue.append(node)
        
        while len(queue) != 0:
            marked[node.data] = True
            node = node.link
            
            if node is None:
                node = queue.pop(0)
                v = node.data
            elif not marked[node.data]:
                ret.append((v, node.data))
                queue.append(self[node.data])
        
        return ret

    def bfs(self, v):
        ret = []
        marked = [False] * self.size
        node = self[v]
        self.bfs_recr(v, node, marked, ret)
        return ret
    
    def bfs_recr(self, v, node, marked, ret):
        while node and not marked[node.data]:
            marked[v] = True
            ret.append((v, node.data))
            
            
        pass
    
    def __getitem__(self, index):
        return self.heads[index]
    
    def __setitem__(self, index, value):
        self.heads[index] = value
    
    def __str__(self):
        ret = ""
        for i, vt in enumerate(self.heads):
            ret += f"v[{i}] = "
            if vt is None or vt.link is None:
                ret += "None\n"
                continue
            
            vt = vt.link
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret
    
if __name__ == "__main__":
    mat = read_input("input.dat")
    print("input matrix")
    print_mat(mat)
    print()
    
    print("adjacency list")
    graph = Graph(mat)
    print(graph)
    
    print("dfs")
    visited = graph.dfs(0)
    print(visited)
    print()
    
    print("bfs")
    visited = graph.bfs(0)
    print(visited)
