from typing import Optional

def read_input(name_file):
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

class Edge:
    def __init__(self, v1=None, v2=None):
        self.marked = False
        self.v1 = v1
        self.v2 = v2
        self.link_v1: Optional[Edge] = None
        self.link_v2: Optional[Edge] = None
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"({self.v1}:{self.v2})"

class GraphMultiListBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")
        
        size = len(mat)
        ret = [Edge(v1=i) for i in range(size)]
        
        for row in range(size):
            for col in range(size):
                if not mat[row][col]:
                    continue
                
                if col < row:
                    edge = ret[col].link_v1
                    
                    while edge.v2 != row or edge.v1 != col:
                        edge = edge.link_v1
                else:
                    edge = Edge(v1=row, v2=col)
                    
                    edge.link_v1 = ret[row].link_v1
                    edge.link_v2 = ret[col].link_v2

                ret[row].link_v1 = edge
                ret[col].link_v2 = edge
                
        return ret

class Graph:
    def __init__(self, heads):
        self.heads = heads
    
    def is_empty(self):
        return not self.heads
    
    def degree(self, v):
        sum_ = 0
        edge = self.heads[v].link_v1
        while edge:
            sum_ += 1
            if edge.v1 == v:
                edge = edge.link_v1
            else:
                edge = edge.link_v2
        return sum_
    
    def explore(self, v):
        ret = []
        node = self.heads[v].link_v1

        while node:
            ret.append(node)
            if node.v1 == v:
                node = node.link_v1
            else:
                node = node.link_v2
        
        return ret
    
    def __len__(self):
        return len(self.heads)

if __name__ == "__main__":
    mat = read_input("input.dat")
    print("Input matrix")
    print_mat(mat)
    
    heads = GraphMultiListBuilder.build(mat)
    graph = Graph(heads)
    print()
    
    for i in range(len(graph)):
        path = graph.explore(i)
        print(f"vertex[{i}]: path = {path}")
    
    print()
    for i in range(len(graph)):
        degree = graph.degree(i)
        print(f"vertex[{i}]: degree = {degree}")