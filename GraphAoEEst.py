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

class HeadNode:
    def __init__(self, id_=0, degree=0):
        self.id_ = id_
        self.degree = degree
        self.link = None
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.id_}"

class Node:
    def __init__(self, vertex=0, duration=0):
        self.vertex = vertex
        self.duration = duration
        self.link = None
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"{self.vertex, self.duration}"

class GraphAoeEstBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        ret = [HeadNode(i) for i in range(size)]
        
        for row in range(size):
            prev = ret[row]
            for col in range(size):
                if not mat[row][col]:
                    continue
                
                node = Node(col, mat[row][col])
                prev.link = node
                prev = node
                ret[col].degree += 1
        
        return ret
    
class GraphAoeEst:
    def __init__(self, list_, mat):
        self.list_ = list_
        self.mat = mat
        
    def outdegree(self, v):
        return sum(self.mat[v])
        
    def __getitem__(self, index):
        return self.list_[index]
    
    def __setitem__(self, index, value):
        self.list_[index] = value
    
    def __len__(self):
        return len(self.list_)
    
    def __str__(self):
        ret = ""
        for i, vt in enumerate(self):
            degree = vt.degree
            ret += f"v[{i}: {degree}] = "
            if vt is None or vt.link is None:
                ret += str(None) + "\n"
                continue
            
            vt = vt.link
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret
    
    def cal_est(self):
        ret = [0] * len(self)
        #self.__build_indegree()
        stack = []
        
        _ = [stack.append(v) for v in self if v.degree == 0]
        print(f"init\t{ret}\t{stack}")
        
        while len(stack) != 0:
            head = stack.pop()
            vt = head
            node = head.link
            
            while node:
                head = self.list_[node.vertex]
                head.degree -= 1
                sum_ = ret[vt.id_] + node.duration
                
                if sum_ > ret[node.vertex]:
                    ret[node.vertex] = sum_
                
                if head.degree == 0:
                    stack.append(head)
                node = node.link
            
            print(f"{vt}\t{ret}\t{stack}")
        
        return ret

if __name__ == "__main__":
    mat_ = read_input("input_aoe_00.dat")
    print("Input matrix")
    print_mat(mat_)
    
    print()
    print("Adjacency list:")
    list_ = GraphAoeEstBuilder.build(mat_)
    graph = GraphAoeEst(list_, mat_)
    print(graph)
    
    print("earliest start time table:")
    est = graph.cal_est()
    
    print()
    print("EST:")
    print(est)