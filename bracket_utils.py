# bracket_utils.py
# Cole Frauzel
# 2022-02-27

# A small collection of methods for parsing expressions with brackets.


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


# Takes in an expression and a starting index and returns the index of the
#   closing bracket for the first occuring open bracket. Validate an expression
#   for balanced brackets before calling this one!
def find_closing_bracket(expr: str, at: int) -> int:
    ret = 0
    stack = []

    for i, c in enumerate(expr[at:]):
        if c == '(':
            stack.append(i)
            continue
        if c == ')':
            x = stack.pop() # popped value is just discarded
            if len(stack) == 0:
                ret = i + at
                break

    return ret


# Strips away the outermost brackets of an expression. Note that it will
#   do this regardless of what's before or after said brackets.
def strip_outer_brackets(expr: str) -> str:
    for i, c in enumerate(expr):
        if c == '(':
            closing = find_closing_bracket(expr, i)
            break
    
    return expr[:i] + expr[i+1:closing] + expr[closing+1:]


# Replaces any square or curly brackets with round brackets for easier parsing.
def replace_square_curly_brackets(expr: str) -> str:
    return expr.replace('{','(').replace('}',')').replace('[','(').replace(']',')')


# Adds a * where a multiplication is denoted by a factor against a bracket.
#   i.e., 2(3+5) -> 2*(3+5)
def insert_multiplication_sign(expr: str) -> str:
    for i, c in enumerate(expr):
        if (c == '(') and (i > 0) and ((expr[i-1].isdigit()) or (expr[i-1] == ')')):
            expr = expr[:i] + '*' + expr[i:]

    return expr

