class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
    
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
                if mat[row][col] == 1:
                    vt.link = Node(col)
                    vt = vt.link
    
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
            print(f"{mat[row][col]}", end=" ")
        print("\b")

if __name__ == "__main__":
    mat = read_input("input_g4.dat")
    print("Input matrix")
    print_mat(mat)
    
    print()
    print("Adjacency list")
    graph = Graph(mat)
    print(graph.heads)
    print(graph)