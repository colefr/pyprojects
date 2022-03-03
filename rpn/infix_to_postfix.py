# infix_to_postfix.py
# 2022-02-28
# Cole Frauzel

# This will convert an expression written in infix notation into postfix
# (or Reverse Polish) notation, and then evaluate it.

# A notable shortcoming is the lack of support for numbers with decimal
# points! (You could still use fractional numbers i.e. instead of 0.25
# you could enter (1/4)... )

import sys
import re
import operator
from bracket_utils import brackets_are_valid

if len(sys.argv) == 1:
    expr = input("Enter the expression: ")
else:
    expr = sys.argv[1]
expr = expr.replace(' ', '')   #remove spaces


def split_into_terms(expr: str) -> list:
    # regexplanaion:
    #       () to include the delimiting characters
    #       [] matches everything insidex
    # filter None since the regex produces some empty elements
    return list(filter(None, (re.split("([\+\-\*\/\^()])", expr) )))


# If there is a number against an open bracket, i.e. 2(3), it will inject
# a '*' between them for easier parsing later. 2(3) -> 2*(3)
def inject_multiplication(terms: list) -> list:
    for i, c in enumerate(terms):
        if c == '(':
            if i > 0 and terms[i-1].isnumeric():
                terms.insert(i, '*')
    return terms


def infix_to_postfix(terms: list) -> list:
    out_stack = []
    oper_stack = []

    precedence = {
        '+' : 1, '-' : 1,
        '*' : 2, '/' : 2,
        '^' : 3
    }

    for i in inject_multiplication(split_into_terms(expr)):

        if i.isnumeric():
            out_stack.append(i)
            continue

        elif i in "+-*/^":
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


def evaluate_postfix_expression(expr: list) -> float:
    stack = []
    left_operand = 0
    right_operand = 0

    ops = {
        '+' : operator.add,     '-' : operator.sub,
        '*' : operator.mul,     '/' : operator.truediv,
        '^' : operator.pow
    }

    for i in expr:
        if i.isnumeric():
            stack.append(int(i))
            continue

        elif i in "+-*/^":
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(ops[i](left_operand, right_operand))
                
        else:
            print("Non numeric/opeator in expression?")
            break

    return stack[0]



if not brackets_are_valid(expr):
    exit()
else:
    for i in infix_to_postfix(expr):
        print(i, end=' ')
    print()
    print(evaluate_postfix_expression(infix_to_postfix(expr)))