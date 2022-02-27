# math_expr_eval_recursive.py
# Cole Frauzel
# 2022-02-27

# A recursive approach to evaluating an arithmetic expression respecting
#   order of operations.

import sys


if len(sys.argv) == 1:
    expr = input("Enter the expression: ")
else:
    expr = sys.argv[1]


def brackets_are_valid(expr: str) -> bool:
    ret = False
    stack = []
    last_open_bracket_pos = 0

    for i, c in enumerate(expr):
        if c == '(':
            stack.append(i)
            continue
        if c == ')':
            try:
                last_open_bracket_pos = stack.pop()
            except IndexError:
                print(f"Closing bracket at {i} has no opening.")
                return False

    if len(stack) == 0:
        return True
    else:
        print(f"Open bracket at {last_open_bracket_pos} has no closing.")
        return False

# 1. Split into terms at + or -
# 2. Evaluate expression in brackets
#   a) if there are brackets within the brackets, evaluate those.
# 3. Evaluate exponents
# 4. Evaluate multiplications/divisions, left-to-right
# 5. Evaluate all evaluated terms, adding/subtracting left-to-right


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


def split_terms(expr: str) -> list:
    terms = []
    last_split = 0
    i = 0

    while i < len(expr):
        if expr[i] == '+' or expr[i] == '-':
            if i == 0:  # don't cut off a - at the very front of the expression
                i = i + 1
            else:
                terms.append(expr[last_split:i])
                last_split = i
                i = i + 1
                
        elif expr[i] == '(':
            closing = find_closing_bracket(expr, i)
            terms.append(expr[last_split:closing + 1])
            last_split = closing + 1
            i = closing

        else:
            i = i + 1

    terms.append(expr[last_split:]) # append the remaining term
    terms = list(filter(None, terms)) # the above code produces empty elements?
                                        # there's gotta be a better fix
                                        # but for now.......

    return terms



if not brackets_are_valid(expr):
    exit()
else:
    for i in split_terms(expr):
        print(i)
        
