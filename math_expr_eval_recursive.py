# math_expr_eval_recursive.py
# Cole Frauzel
# 2022-02-27

# A recursive approach to evaluating an arithmetic expression respecting
#   order of operations.

import sys
from bracket_utils import *
import re

if len(sys.argv) == 1:
    expr = input("Enter the expression: ")
else:
    expr = sys.argv[1]
expr = expr.replace(' ', '')   #remove spaces
expr = replace_square_curly_brackets(expr)

# 1. Split into terms at + or -
# 2. Evaluate expression in brackets
#   a) if there are brackets within the brackets, evaluate those.
# 3. Evaluate exponents
# 4. Evaluate multiplications/divisions, left-to-right
# 5. Evaluate all evaluated terms, adding/subtracting left-to-right


def split_into_terms(expr: str) -> list:
    terms = []
    last_split = 0
    i = 0

    while i < len(expr):
        if expr[i] in "+-":
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


def multiply_divide_within_term(term: str) -> int:
    factors = []
    last_split = 0

    for i, c in enumerate(term):
        if c in "*/":
            factors.append(term[last_split:i])
            last_split = i
    factors.append(term[last_split:])

    ret = 0
    for i in factors:
        if i[0] not in "*/":    # first case, no leading operator
            ret = int(i)
        elif i[0] == '*':
            ret = ret * int(i[1:])
        elif i[0] == '/':
            ret = ret / int(i[1:])

    return ret


def evaluate(expr: str) -> int:
    terms = split_into_terms(expr)
    evaluated_terms = []
    for term in terms:
        
        term = insert_multiplication_sign(term)
        print(term)
        
        if '(' in term or ')' in term:
            i = 0

            while i < len(term):
                if term[i] == '(':
                    closing = find_closing_bracket(term, i)
                    #print(term[i+1:closing])
                    evaluate(term[i+1:closing])
                    i = closing
                    continue
                else:
                    i = i + 1

        else:
            evaluated_terms.append(multiply_divide_within_term(term))

    print(evaluated_terms)
    print(sum(evaluated_terms))
    return sum(evaluated_terms)

if not brackets_are_valid(expr):
    exit()
else:
    print(evaluate(expr))
