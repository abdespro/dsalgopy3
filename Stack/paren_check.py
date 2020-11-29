# Using Stack 
# to check whether a parenthesis-string is balanced or not

# Balanced parenthesis: "[{()}]"
# Non-Balanced parenthesis: "{{}"
# edge case: ")]]"

# by abir
# Nov 29, 2020

from stack import Stack

def is_p_match(p1, p2):
    if p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False
    
def is_pstr_balanced(pstr):
    pstack = Stack()
    is_balanced = True
    
    for p in pstr:
        if p in "[{(":
            pstack.push(p)
        else:
            if pstack.is_empty():
                is_balanced = False
            else:
                top_item = pstack.pop()
                if not is_p_match(top_item, p):
                    is_balanced = False
    
    if pstack.is_empty() and is_balanced:
        return True
    else:
        return False
    
def main():
    print("parenthesis balanced: ", is_pstr_balanced("(()"))

if __name__ == "__main__":
    main()
