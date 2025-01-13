class Graph:
  def __init__(self):
    self.nodes = [] # list of nodes
    self.matrix = [] # the adjacency matrix
    self.node_count = 0 # to store the no. of nodes

  def print_graph(self):
    print('List of nodes:',*self.nodes)
    print('Adjacency matrix:')
    for row in self.matrix:
      print(*row,sep=' ')

  def add_node(self,node):
    if node in self.nodes:
      print(node,"already exists")
    else:
      self.nodes.append(node)
      self.node_count += 1
      # adding an extra column for the new node
      for row in self.matrix:
        row.append(0)
      # adding an extra row for the new node
      self.matrix.append([0]*self.node_count)

  def add_edge(self, node1, node2,weight):
    if node1 not in self.nodes or node2 not in self.nodes:
      absent_node='Either node' if node1 not in self.nodes and node2 not in self.nodes else (node1 if node1 not in self.nodes else node2)
      print(absent_node,"does not exist")
    else:
      node1_index = self.nodes.index(node1)
      node2_index = self.nodes.index(node2)
      self.matrix[node1_index][node2_index]=weight
      self.matrix[node2_index][node1_index]=weight # for a directed graph, this line is to be omitted

  def delete_node(self,node):
    if node not in self.nodes:
      print(node,"does not exist.")
    else:
      node_index = self.nodes.index(node)
      self.nodes.remove(node)
      self.node_count -= 1
      self.matrix.pop(node_index)
      for row in self.matrix:
        row.pop(node_index)

  def delete_edge(self,node1,node2):
    if node1 not in self.nodes or node2 not in self.nodes:
      absent_node='Either node' if node1 not in self.nodes and node2 not in self.nodes else (node1 if node1 not in self.nodes else node2)
      print(absent_node,"does not exist")
    else:
      node1_index = self.nodes.index(node1)
      node2_index = self.nodes.index(node2)
      self.matrix[node1_index][node2_index]=0
      self.matrix[node2_index][node1_index]=0 # for a directed graph, this line is to be omitted


graph=Graph()
print("Before adding nodes,")
print('List of nodes:',graph.nodes)
print('Adjacency matrix:',graph.matrix)
for i in ['A','B','C','E','F']:
  graph.add_node(i)
print("After adding nodes:")
graph.print_graph()
print('After adding edge:')
graph.add_edge('A','C',5)
graph.add_edge('D','A',10)
graph.add_edge('D','C',3)
graph.add_edge('B','A',6)
graph.print_graph()
graph.delete_node('B')
graph.delete_node("D")
graph.print_graph()
print("Before deleting edges:")
graph.print_graph()
print("After deleting edges:")
graph.delete_edge('A','B')
graph.print_graph()