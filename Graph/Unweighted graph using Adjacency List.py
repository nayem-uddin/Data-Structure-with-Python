class Graph:
    def __init__(self):
        self.graph = dict()

    def add_node(self,node):
        if node in self.graph.keys():
            print(node,"already exists")
        else:
            self.graph[node]=[]

    def add_edge(self,node1,node2):
        if node1 not in self.graph.keys() or node2 not in self.graph.keys():
            absent_node='Either of the nodes' if node1 not in self.graph.keys() and node2 not in self.graph.keys() else (node1 if node1 not in self.graph.keys() else node2)
            print(absent_node,"does not exist")
        else:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1) # for directed graph, this line is to be omitted
    
    def delete_node(self,node):
        if node not in self.graph.keys():
            print(node,"does not exist")
        else:
            self.graph.pop(node)
            for key in self.graph:
                if node in self.graph[key]:
                    self.graph[key].remove(node)

    def delete_edge(self,node1,node2):
        if node1 not in self.graph.keys() or node2 not in self.graph.keys():
            absent_node='Either of the nodes' if node1 not in self.graph.keys() and node2 not in self.graph.keys() else (node1 if node1 not in self.graph.keys() else node2)
            print(absent_node,"does not exist")
        else:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
                self.graph[node2].remove(node1) # for directed graph, the following line is to be omitted
            else:
                print(node2, ' is not connected to ',node1)

    def print_graph(self):
        print('Adjacency list:',self.graph)


graph=Graph()
for i in ['A','B','C','D']:
    graph.add_node(i)
graph.add_node('D')
print('After adding nodes:')
graph.print_graph()
print('After adding edges:')
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('B','D')
graph.add_edge('C','D')
graph.add_edge('E','A')
graph.print_graph()
print('After deleting nodes:')
graph.delete_node('E')
graph.delete_node('D')
graph.print_graph()
print('After deleting edges:')
graph.delete_edge('A','B')
graph.delete_edge('A','E')
graph.print_graph()