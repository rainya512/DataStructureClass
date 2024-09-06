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
    def __init__(self, elem):
        self.elem = elem
        self.link: Optional[Node] = None
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"

class Head(Node):
    def __init__(self, id):
        super().__init__(id)
        self.indegree = 0
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.elem}"

class GraphListBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")
        
        size = len(mat)
        ret = [Head(i) for i in range(size)]
        for row in range(size):
            prev = ret[row]
            for col in range(size):
                if not mat[row][col]:
                    continue
                
                node = Head(col)
                prev.link = node
                prev = node 
                ret[col].indegree += 1
        return ret

class Graph:
    def __init__(self, heads):
        self.heads = heads
        self.size = len(self.heads)
        
    def sort_topology(self):
        ret = []
        stack = []
        _ = [stack.append(v) for v in self.heads if v.indegree == 0]

        while len(stack) != 0:
            vt = stack.pop()
            ret.append(vt)
            
            while vt:
                node = self.heads[vt.elem]
                node.indegree -= 1
                vt = vt.link
            
            if len(stack) == 0:
                _ = [stack.append(v) for v in self.heads if v.indegree == 0]
        
        return ret

    def __str__(self):
        ret = ""
        for i, vt in enumerate(self.heads):
            ret += f"v[{i}: {vt.indegree}] = "
            if vt is None or vt.link is None:
                ret += "None\n"
                continue
            
            vt = vt.link
            while vt:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret

if __name__ == "__main__":
    mat = read_input("input_00.dat")
    print("Input matrix")
    print_mat(mat)
    print()
    
    print("Adjacency list")
    heads = GraphListBuilder.build(mat)
    graph = Graph(heads)
    print(graph)
    
    print("Topology list")
    topology = graph.sort_topology()
    print(topology)