# Stack 
# Using LinkedList

# by abir
# Nov 30, 2020

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def push(self, data):
        self.length += 1
        new_node = Node(data)
        last_node = self.head
        self.head = new_node
        self.head.next = last_node
        
    def pop(self):
        if self.head is not None:
            self.length -= 1
            node_to_popped = self.head
            self.head = self.head.next
            return node_to_popped.data
        else:
            return -1
        
    def peek(self):
        return self.head.data
    
    def get_stack(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def stack_size(self):
        return self.length
    
    def is_empty(self):
        return self.head == None
            
def main():    
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    
    print("Stack:")
    s.get_stack()
    print()
    print("is Stack empty? ")
    print(s.is_empty())
    print()
    print("Stack size: ")
    print(s.stack_size())
    print()
    print("Popped item: ")
    print(s.pop()) 
    print()
    print("Stack now: ")
    s.get_stack()
    print()
    print("Stack size now: ")
    print(s.stack_size())
    print()
    print("Popped item: ")
    print(s.pop()) 
    print()
    print("Popped item: ")
    print(s.pop()) 
    print()
    print("Stack size now: ")
    print(s.stack_size())
    print()
    print("is Stack empty? ")
    print(s.is_empty())
    print()

if __name__ == "__main__":
    main()
