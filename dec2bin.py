# Using Stack 
# to convert integer decimal values to binary

# by abir
# Nov 30, 2020

"""
Example: 42
42//2 = 21 r 0
21//2 = 10 r 1
10//2 = 5  r 0
5//2  = 2  r 1
2//2  = 1  r 0
1//2  = 0  r 1
"""

from stack import Stack

def dec_to_bin(decimal):
    s = Stack()
    while decimal > 0:
        s.push(decimal%2)
        decimal //= 2
    
    binary = []
    while not s.is_empty():
        binary.append(str(s.pop()))
    return "".join(binary)
        
print(dec_to_bin(42))
print(dec_to_bin(424))
