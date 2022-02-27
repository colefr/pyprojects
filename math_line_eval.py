# math_line_eval.py
# Cole Frauzel
# 2022-02-27

# Takes in a string containting a math expression and parses it respecting
#   order of operations.
# This is just so I can practice making a parser and evaluator. I'll be using
#   the results to make my boolean logic evaluator.

import re
import sys

# debug -----------------------------------------------------------------------
""" print(f"Arg count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Arg {i}: {arg}") """
# -----------------------------------------------------------------------------


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
            #print(f"push ( at {i}")
            stack.append(i)
            continue
        if c == ')':
            #print(f"pop ) at {i}")
            try:
                last_open_bracket_pos = stack.pop()
            except IndexError:
                print(f"Closing bracket at {i} has no opening.")
                return False
        
    #print(stack)

    if len(stack) == 0:
        return True
    else:
        print(f"Open bracket at {last_open_bracket_pos} has no closing.")
        return False


def pair_brackets(expr: str) -> list:
    ret = []
    stack = []

    for i, c in enumerate(expr):
        pair = [0,0]
        if c == '(':
            stack.append(i)
            continue
        if c == ')':
            pair[0] = stack.pop()
            pair[1] = i
            ret.append(pair)

    return ret


def order_by_brackets(expr: str, pair_list: list) -> list:
    ret = []
    for i in pair_list:
        ret.append(expr[i[0]+1 : i[1]])
    return ret


def extract_terms(expr: str) -> list:
    ret = re.split("[\+\-]", expr)  #splits sting at + or - signs (via regex)
    return ret
        


if not brackets_are_valid(expr):
    exit()
else:
    bracket_pairs = pair_brackets(expr)
    eval_order_by_brackets = order_by_brackets(expr, bracket_pairs)
    
    #print(extract_terms(expr))
    print(bracket_pairs)
    print(eval_order_by_brackets)
