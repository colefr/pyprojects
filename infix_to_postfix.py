# infix_to_postfix.py
# 2022-02-28
# Cole Frauzel

# This will convert an expression written in infix notation into postfix
# (or Reverse Polish) notation, and then evaluate it.

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
    return list(filter(None, (re.split("([\+\-\*\/()])", expr) )))


def infix_to_postfix(terms: list) -> list:
    out_stack = []
    oper_stack = []

    for i in split_into_terms(expr):

        if i.isnumeric():
            out_stack.append(i)
            continue

        elif i in "+-*/":
            if len(oper_stack) > 0 and oper_stack[len(oper_stack)-1] != '(' and i in "+-":
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
        '*' : operator.mul,     '/' : operator.truediv
    }

    for i in expr:
        if i.isnumeric():
            stack.append(float(i))
            continue

        elif i in "+-*/":
            right_operand = float(stack.pop())
            left_operand = float(stack.pop())
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