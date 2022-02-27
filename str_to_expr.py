# str_to_expr.py
# Cole Frauzel
# 2022-02-27

# Solve a simple (addition/subtraction) expression from a string

import sys

if len(sys.argv) == 1:
    expr = input("Enter the expression: ")
else:
    expr = sys.argv[1]


def split_terms(expr: str) -> list:
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


def terms_to_numbers(terms: list) -> list:
    values = []

    for i in terms:
        if i[0] not in "+-":    # no leading sign (only case should be first term +)
            values.append(int(i))
        elif i[0] == "-":       # negative term
            values.append(int(i[1:]) * -1)
        else:                   # only case should be positive terms (not first)
            values.append(int(i[1:]))

    return values


print(expr)
print(split_terms(expr))
print(terms_to_numbers(split_terms(expr)))
print(sum(terms_to_numbers(split_terms(expr))))

