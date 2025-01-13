class Graph:
    def __init__(self):
        self.graph = dict()
        
    def add_node(self,node):
        if node in self.graph.keys():
            print(node,"already exists")
        else:
            self.graph[node]=[]

    def add_edge(self,node1,node2,weight):
        if node1 not in self.graph.keys() or node2 not in self.graph.keys():
            absent_node='Either of the nodes' if node1 not in self.graph.keys() and node2 not in self.graph.keys() else (node1 if node1 not in self.graph.keys() else node2)
            print(absent_node,"does not exist")
        else:
            list1=[node2,weight]
            self.graph[node1].append(list1)
            # for directed graph, the following two lines are to be omitted
            list2=[node1,weight]
            self.graph[node2].append(list2)
    
    def delete_node(self,node):
        if node not in self.graph.keys():
            print(node,"does not exist")
        else:
            self.graph.pop(node)
            for key in self.graph:
                for cn in self.graph[key]: # looping through the node-weight pairs
                    if node in cn:
                        self.graph[key].remove(cn)
                        break
    
    def delete_edge(self,node1,node2,weight):
        if node1 not in self.graph or node2 not in self.graph:
            absent_node='Either of the nodes' if node1 not in self.graph.keys() and node2 not in self.graph.keys() else (node1 if node1 not in self.graph.keys() else node2)
            print(absent_node,"does not exist")
        else:
            temp1=[node2,weight]
            temp2=[node1,weight] # for directed graph, this line is to be omitted
            if temp1 in self.graph[node1]:
                self.graph[node1].remove(temp1)
                self.graph[node2].remove(temp2) # for directed graph, this line is to be omitted

    def print_graph(self):
        print('Adjacency list:',self.graph)


graph=Graph()
for i in ['A','B','C','D']:
    graph.add_node(i)
graph.add_node('D')
print('After adding nodes:')
graph.print_graph()
print('After adding edges:')
graph.add_edge('A','B',5)
graph.add_edge('A','C',10)
graph.add_edge('B','D',6)
graph.add_edge('C','D',3)
graph.add_edge('E','A',2)
graph.print_graph()
print('After deleting nodes:')
graph.delete_node('E')
graph.delete_node('D')
graph.print_graph()
print('After deleting edges:')
graph.delete_edge('A','E',5)
graph.delete_edge('A','B',5)
graph.delete_edge('A','C',5)
graph.print_graph()