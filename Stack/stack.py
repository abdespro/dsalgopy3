# Stack implementation 
# using python built-in list data type

# Stack methods: push(), pop(), peek()
# more methods: is_empty(), stack_size(), get_stack()

# by abir
# Nov 29, 2020

class Stack:
    def __init__(self):
        self.stack = list()
        self.NumOfItems = 0
        
    def push(self, data):
        self.stack.append(data)
        self.NumOfItems += 1
        
    def pop(self):
        if not self.is_empty():
            self.NumOfItems -= 1
            return self.stack.pop()
        else:
            return -1
        
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return self.NumOfItems
    
    def get_stack(self):
        return self.stack
    
    
# test the implementation
def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push('php')
    s.push('python')
    s.push('cpp')
    s.push('c')

    print("is s empty? : ", s.is_empty())
    print("s: ", s.get_stack())
    print("size of s: ", s.stack_size())
    print("peek s: ", s.peek())

    print()

    print("Last in first out element: ", s.pop())
    print("is s empty? : ", s.is_empty())
    print("s: ", s.get_stack())
    print("size of s: ", s.stack_size())
    print("peek s: ", s.peek())

    print()

    for itervar in range(0, 6):
        print("Last in first out element: ", s.pop())
        print()

    print("is s empty? : ", s.is_empty())

if __name__ == "__main__":
    main()
