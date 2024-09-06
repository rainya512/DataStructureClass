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
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.u, self.v, self.w}"

class Graph:
    def __init__(self, mat):
        self.mat = mat
        self.list_ = []
        self.__build()
    
    def __build(self):
        for r in range(len(self.mat)):
            for c in range(len(self.mat[0])):
                if not self.mat[r][c]:
                    continue
                if c <= r:
                    continue
                self.list_.append(Edge(r, c, self.mat[r][c]))
    
    def __str__(self):
        ret = ""
        for i, edge in enumerate(self.list_):
            ret += f"[{i}] = {edge}\n"
        return ret
    
    def find(self, parent, i):
        while parent[i] >= 0:
            i = parent[i]
        return i
    
    def union(self, root, u, v):
        sum = root[u] + root[v]
        if root[u] > root[v]:
            root[u], root[v] = v, sum
        else:
            root[v], root[u] = u, sum
    
    def kruskal(self):
        ret = []
        n = len(self.mat)
        root = [-1] * n
        self.list_.sort(key= lambda Edge: Edge.w)
        
        i = 0
        while len(ret) < n-1:
            edge = self.list_[i]
            if self.find(root, edge.u) != self.find(root, edge.v):
                self.union(root, edge.u, edge.v)
                print(f"[{i+1}] accept: {edge}")
                ret.append(edge)
            else:
                print(f"[{i+1}] reject: {edge}")
            i += 1
        
        return ret

if __name__ == "__main__":
    mat_ = read_input("input.dat")
    print("Input matrix")
    print_mat(mat_)
    print()
    
    print("Graph's edges")
    graph = Graph(mat_)
    print(graph)
    
    print("Kruskal's Algorithm:")
    mst = graph.kruskal()
    print()
    
    print("Minimum Spanning Tree:")
    for i in mst:
        print(i)