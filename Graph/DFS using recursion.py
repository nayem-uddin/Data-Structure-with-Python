# Here, DFS is implemented for adjacency list representation
class Graph:
    def __init__(self):
        self.graph = dict()
        self.visited=list()
        self.unvisited=list(self.graph.keys())

    def add_node(self,node):
        if node in self.graph.keys():
            print(node,"already exists")
        else:
            self.graph[node]=[]
            self.unvisited.append(node)

    def add_edge(self,node1,node2):
        if node1 not in self.graph.keys() or node2 not in self.graph.keys():
            absent_node='Either of the nodes' if node1 not in self.graph.keys() and node2 not in self.graph.keys() else (node1 if node1 not in self.graph.keys() else node2)
            print(absent_node,"does not exist")
        else:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1) # for directed graph, this line is to be omitted

    def visit(self,node):
        assert node in self.graph, f'{node} is not present in the graph'
        self.DFS(node)
        print(*self.visited,sep=' ')

    def DFS(self,node):
        if node not in self.visited:
            self.visited.append(node)
            if node in self.unvisited:
                self.unvisited.remove(node)
            for n in self.graph[node]:
                self.DFS(n) # for weighted graph, write n[0] instead of n
                
    def is_connected(self):
        if not self.unvisited:
            return True
        return False
    
    def visit_disconnected(self):
        while self.unvisited:
            temp=self.visited
            self.visited=list()
            print('Next connected nodes')
            for i in self.unvisited:
                if i not in self.visited:
                    self.DFS(i)
            self.visit(self.visited[0])
        self.unvisited=temp

graph=Graph()
for i in ['A','B','C','D','E','F','G']:
    graph.add_node(i)
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('B','D')
graph.add_edge('C','D')
graph.add_edge('E','F')
# graph.visit('B')
graph.visit('A')
# graph.visit('K')
graph.visit_disconnected()
print(graph.is_connected())