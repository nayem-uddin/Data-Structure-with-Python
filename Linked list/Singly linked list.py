# Step 1
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

# Step 2
class LinkedList:
    def __init__(self):
        self.head = None

    # for traversing through and printing the nodes
    def print_LL(self):
        if self.head==None:
          # the if-statement is required if you want a message to show up when the user wants to print the linked list while it is empty. Otherwise, only the statements under the else condition will suffice.
            print("Linked list is empty")
        else:
            n = self.head
            while n!=None:
                print(n.data,end=' ')
                if n.next:
                    print('->',end=' ')
                n = n.next

    # for adding a new element at the beginning of the linked list
    def add_begin(self,data):
        new_node = Node(data) # creating the new node to insert at the beginning
        new_node.next=self.head # changing the reference of the new node to the reference of the first node (the then "head") of the original linked list
        self.head = new_node # changing the head value to the value of the new node, as the new node is the first node (head) now

    # for adding a new element at the end of the linked list
    def add_end(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
        else:
            n = self.head
            while n.next!=None:
                n = n.next # traverse through the list until the last element is reached
            n.next = new_node

    # for adding a new element after a specific node
    def add_after(self,data,x):
        n = self.head
        while n!=None:
            if n.data==x:
                break
            n=n.next
        if n==None:
            print("Element not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # for adding a new node before a specific node
    def add_before(self,data,x):
        if self.head==None:
            print("Linked list is empty")
            return
        elif self.head.data==x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            n=self.head
            while n.next!=None:
                if n.next.data==x:
                    break
                n=n.next
            if n.next==None:
                print("Element not found")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    # for deleting head
    def delete_head(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

    # for deleting tail
    def delete_tail(self):
        if self.head==None:
            print("Linked list is empty")
        elif self.head.next==None:
            self.head = None
        else:
            n = self.head
            while n.next.next!=None:
                n = n.next
            n.next = None
            
    # for deleting node
    def delete_node(self,data):
        if self.head==None:
            print("Linked list is empty")
        elif self.head.data==data:
            self.head = self.head.next
        else:
            n = self.head
            while n.next.next!=None:
                if n.next.data==data:
                    break
                n = n.next
            if n.next.next==None:
                print("Element not found")
            else:
                n.next=n.next.next

ll=LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)
# ll.print_LL()
ll.add_end(10)
ll.add_end(20)
ll.add_end(30)
ll.add_after(40,20)
ll.add_after(50,60)
ll.add_before(40,20)
ll.add_before(50,60)
ll.delete_head()
ll.delete_tail()
ll.delete_node(10)
ll.delete_node(50)
ll.print_LL()