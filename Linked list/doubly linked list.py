# step 1
class node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None


# step 2
class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    
  def forward_traverse(self): # forward traversal operation
    n=self.head
    while n!=None:
      print(n.data,end=' ')
      if n.next:
        print('->',end=' ')
      n=n.next
    print()

  def backward_traverse(self): # backward traversal operation
    n=self.tail
    while n!=None:
      print(n.data,end=' ')
      if n.prev:
        print('->',end=' ')
      n=n.prev
    print()

  def insert_head(self,data): # add a new node at the beginning of the linked list
    new_node=node(data)
    if self.head==None:
      self.head= new_node
      self.tail=new_node
    else:
      new_node.next=self.head
      self.head.prev=new_node
      self.head=new_node

  def insert_tail(self,data): # add a new node at the end of the linked list
    new_node=node(data)
    if self.head==None:
      self.head=new_node
    else:
      new_node.prev=self.tail
      self.tail.next=new_node
    self.tail=new_node

  def add_after(self,data,x): # add a node after the node with the data x
    n=self.head
    while n!=None:
      if n.data==x:
        break
      n=n.next
    if n==None:
      print("Node not found.")
    else:
      new_node=node(data)
      new_node.next=n.next
      new_node.prev=n
      if n.next!=None:
        n.next.prev=new_node
      n.next=new_node

  def add_before(self,data,x): # add a node before the node with the data x
    n=self.head
    while n!=None:
      if n.data==x:
        break
      n=n.next
    if n==None:
      print("Node not found.")
    else:
      new_node=node(data)
      new_node.next=n
      new_node.prev=n.prev
      if n.prev!=None:
        n.prev.next=new_node
      else:
        self.head=new_node
      n.prev=new_node

  def delete_head(self): # delete the first node
    if self.head==None:
      print("Linked list is empty.")
    elif self.head.next==None:
      self.head=None
    else:
      self.head=self.head.next
      self.head.prev=None

  def delete_tail(self): # delete the last node
    if self.head==None:
      print("Linked list is empty.")
    elif self.head.next==None:
      self.head=None
    else:
      self.tail=self.tail.prev
      self.tail.next=None

  def delete_node(self,data): # delete the node with the given data
    if self.head==None:
      print("Linked list is empty.")
    elif self.head.next==None:
      if self.head.data==data:
        self.head=None
      else:
        print("Node not found.")
    else:
      if self.head.data==data:
        self.head=self.head.next
        self.head.prev=None
      else:
        n=self.head.next
        while n!=None:
          if n.data==data:
            break
          n=n.next
        if n==None:
          print("Node not found.")
        else:
          n.prev.next=n.next
          if n.next!=None:
            n.next.prev=n.prev
          else:
            self.tail=n.prev


ll=DoublyLinkedList()
ll.insert_head(30)
ll.insert_head(20)
ll.insert_head(10)
ll.insert_tail(40)
ll.insert_tail(50)
print("Forward traversal:",end=' ')
ll.forward_traverse() # expected output is: 10 20 30 40 50
print("Backward traversal:",end=' ')
ll.backward_traverse() # expected output is: 50 40 30 20 10
ll.add_after(45,40)
ll.add_before(25,30)
ll.forward_traverse() # expected output is: 10 20 25 30 40 45 50
ll.backward_traverse() # expected output is: 50 45 40 30 25 20 10
ll.delete_head()
ll.forward_traverse() # expected output is: 20 30 40 50
ll.backward_traverse() # expected output is: 50 40 30 20
ll.delete_tail()
ll.forward_traverse() # expected output is: 10 20 30 40
ll.backward_traverse() # expected output is: 40 30 20 10
ll.delete_node(10)
ll.delete_node(50)
ll.delete_node(30)
ll.forward_traverse() # expected output is: 20 40
ll.backward_traverse() # expected output is: 40 20
ll.delete_node(10) # will show a "Node not found" message