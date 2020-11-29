# implementation of linkedlist
# Singly Linkedlist: linear data structure 
# by abir
# 29 Nov, 2020

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.NumOfElements = 0

    def __len__(self):
        return self.NumOfElements
    
    def add_at_beginning(self, data):
        self.NumOfElements += 1
        New_Node = Node(data)
        
        if not self.head:
            self.head = New_Node
        else:
            New_Node.next = self.head
            self.head = New_Node
    
    def add_at_end(self, data):
        self.NumOfElements += 1
        New_Node = Node(data)
        temporary_node = self.head
        
        while temporary_node.next is not None:
            temporary_node = temporary_node.next
            
        temporary_node.next = New_Node
        
    def __str__(self):
        temporary_node = self.head
        all_data = []
        for e in range(0, self.NumOfElements):
            all_data.append(temporary_node.data)
            temporary_node = temporary_node.next
            
        return f"{all_data}"
    
    def remove(self, data):
        if self.head is None:
            return
        
        self.NumOfElements -= 1
        temporary_node = self.head
        previous_node = None
        
        while temporary_node.next is not None and temporary_node.data != data:
            previous_node = temporary_node
            temporary_node = temporary_node.next
        
        if temporary_node is None:
            return
        
        if previous_node is None:
            self.head = temporary_node.next
        else:
            previous_node.next = temporary_node.next 
        
    
l = LinkedList()

l.add_at_beginning(5)
l.add_at_beginning(6)
l.add_at_beginning(7)
l.add_at_beginning(8)
l.add_at_beginning('name')

l.add_at_end(78)
l.add_at_end('last')

print(l)

l.remove(7)
l.remove(8)

print(l)

                
