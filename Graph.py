class UndiGraph:
    def __init__(self, size) -> None:
        self.graph = [[0] * size for _ in range(size)]
    
    def insert_edge(self, src, dst, elem=1):
        self.graph[src][dst] = elem
        self.graph[dst][src] = elem
    
    def remove_edge(self, src, dst, elem=0):
        self.graph[src][dst] = elem
        self.graph[dst][src] = elem
    
    def degree(self, v):
        d = 0
        for i in range(len(self.graph)):
            d += self.graph[v][i]
            
        return d
    
    def __getitem__(self, coords):
        row, col = coords
        return self.graph[row][col]
    
    def __setitem__(self, coords, elem):
        row, col = coords
        self.graph[row][col] = elem
    
    def __len__(self):
        return len(self.graph)
    
    def __str__(self):
        ret = ""
        for row in range(len(self.graph)):
            ret += str(self.graph[row]) + "\n"
        return ret.strip() 

if __name__ == "__main__":
    VERTICES = 4
    graph = UndiGraph(VERTICES)
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(0, 3)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 3)
    
    print("graph")
    for row in range(len(graph)):
        for col in range(len(graph)):
            print(graph[row, col], end=" ")
        print()
    
    print()
    v = 0
    print(f"degree[{v}] = {graph.degree(v)}")
    v = 3
    print(f"degree[{v}] = {graph.degree(v)}")
    
    print()
    print("graph")
    print(graph)