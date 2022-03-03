# postfix_utils.py
# Cole Frauzel
# 2022-03-03

# A collection of methods for converting infix to postfix notation

import re

# Takes in an expression as a string and checks if the brackets are
#   balanced. Returns True if no issues found; returns False if
#   unbalanced brackets are detected and prints where it found
#   a mismatch. (Though it might not be the only mismatch!)
def brackets_are_valid(expr: str) -> bool:
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


# Replaces any square or curly brackets with round brackets for easier parsing.
def replace_square_curly_brackets(expr: str) -> str:
    return expr.replace('{','(').replace('}',')').replace('[','(').replace(']',')')


# Splits a string by delimiters
def split_into_terms(expr: str, delimits: list) -> list:
    # regexplanaion:
    #       () to include the delimiting characters
    #       [] matches everything insidex
    # filter None since the regex produces some empty elements
    pattern = "([()"
    for i in delimits:
        pattern = pattern + '\\' + i
    pattern = pattern + "])"
    return list(filter(None, (re.split(pattern, expr) )))


# If there is a number against an open bracket, i.e. 2(3), it will inject
# a '*' between them for easier parsing later. 2(3) -> 2*(3)
def inject_multiplication(terms: list) -> list:
    for i, c in enumerate(terms):
        if c == '(':
            if i > 0 and terms[i-1].isnumeric():
                terms.insert(i, '*')
    return terms


# Convert a list of terms in infix notation to a list of terms in postfix
# based on a dict contaning the order of precedence on the operators,
# where higher number = higher precedence.
#
# An example of a precedence dict would look like:
# precedence = {
#         '+' : 1, '-' : 1,
#         '*' : 2, '/' : 2,
#         '^' : 3
#     }
#
# set inject_mult to place *'s before multiplier brackets. i.e. 2(3) -> 2*(3) 
def infix_to_postfix(terms: list, precedence: dict, inject_mult: bool = False) -> list:
    out_stack = []
    oper_stack = []

    if inject_mult:
        terms = inject_multiplication(terms)
    
    for i in terms:

        if i.isnumeric():
            out_stack.append(i)
            continue

        elif i in precedence:
            if len(oper_stack) > 0:
                top = oper_stack[-1]
            if len(oper_stack) > 0 and top != '(' and precedence[top] >= precedence[i]:
                out_stack.append(oper_stack.pop())
            oper_stack.append(i)
        
        elif i == '(':
            oper_stack.append(i)

        elif i == ')':
            while oper_stack[len(oper_stack)-1] != '(':
                out_stack.append(oper_stack.pop())
            x = oper_stack.pop()

        else:
            print("Non numeric/opeator in expression?")
            break
    
    while len(oper_stack) > 0:
        out_stack.append(oper_stack.pop())

    return out_stack

