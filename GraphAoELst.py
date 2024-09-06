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

class GraphAoeLstBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        ret = [HeadNode(i) for i in range(size)]
        
        for col in range(size):
            prev = ret[col]
            for row in range(size):
                if not mat[row][col]:
                    continue
                
                node = Node(row, mat[row][col])
                prev.link = node
                prev = node
                ret[row].degree += 1
        
        return ret

class GraphAoeLst:
    def __init__(self, list_, mat, est):
        self.list_ = list_
        self.mat = mat
        self.est = est
        
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
    
    def cal_lst(self):
        ret = [max(self.est)] * len(self)
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
                sub_ = ret[vt.id_] - node.duration
                
                if sub_ < ret[node.vertex]:
                    ret[node.vertex] = sub_
                
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
    print("EST:")
    (*est,) = 0, 6, 4, 5, 7, 7, 16, 14, 18
    print(est)
    
    list_ = GraphAoeLstBuilder.build(mat_)
    graph = GraphAoeLst(list_, mat_, est)
    
    print()
    print("Inverse Adjacency list:")
    print(graph)
    
    print("Latest start time table:")
    lst = graph.cal_lst()
    print(lst)