# str_to_expr.py
# Cole Frauzel
# 2022-02-27

# Solve a simple 4-function expression from a string (no brackets)

import sys

if len(sys.argv) == 1:
    expr = input("Enter the expression: ")
else:
    expr = sys.argv[1]

expr = expr.replace(' ', '')   #remove spaces

def split_into_terms(expr: str) -> list:
    terms = []
    last_split = 0

    for i, c in enumerate(expr):
        if i == 0:
            continue
        else:
            if c in "+-":
                terms.append(expr[last_split:i])
                last_split = i
    terms.append(expr[last_split:])

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




print(expr)
terms = split_into_terms(expr)
print(terms)

evaluated_terms = []
for i in terms:
    evaluated_terms.append(multiply_divide_within_term(i))
print(evaluated_terms)

final_eval = sum(evaluated_terms)
print(final_eval)


