# brackets_are_valid.py
# Cole Frauzel
# 2022-02-27

# Takes in an expression as a string and checks if the brackets are
#   balanced. Returns True if no issues found; returns False if
#   unbalanced brackets are detected and prints where it found
#   a mismatch. (Though it might not be the only mismatch!)

def brackets_are_valid(expr: str) -> bool:
    ret = False
    stack = []
    last_open_bracket_pos = 0

    for i, c in enumerate(expr):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                print(f"Closing bracket at {i} has no opening.")
                print(expr)
                print(" "*i + "^ here.")
                return False
            else:
                last_open_bracket_pos = stack.pop()
                

    if len(stack) == 0:
        return True
    else:
        print(f"Open bracket at {last_open_bracket_pos} has no closing.")
        print(expr)
        print(" "*last_open_bracket_pos + "^ here.")
        return False

