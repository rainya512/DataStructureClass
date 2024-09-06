class Edge:
    def __init__(self, v1=None, v2=None):
        self.marked = False
        self.v1 = v1
        self.v2 = v2
        self.link_v1 = None
        self.link_v2 = None
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.v1}:{self.v2}"

def read_input(name_file):
    mat = []
    with open(name_file) as f:
        for line in f:
            (*row, ) = map(int, line.split())
            mat.append(row)
    
    return mat

class Builder:
    @staticmethod
    def build(mat):
        size = len(mat)
        ret = [Edge(v1=i) for i in range(size)]
        edges = []
        
        for row in range(size):
            for col in range(size):
                if not mat[row][col]:
                    continue
                
                if col > row:
                    edges.append(Edge(v1=row, v2=col))
        
        return edges

if __name__ == "__main__":
    mat = read_input("input_test.dat")
    heads = Builder.build(mat)
    for i in range(len(heads)):
        print(f"[{i}]: {heads[i]}")