# str_to_expr.py
# Cole Frauzel
# 2022-02-27

# Solve a simple (addition/subtraction) expression from a string

import sys
import re

if len(sys.argv) == 1:
    expr = input("Enter the expression: ")
else:
    expr = sys.argv[1]

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

print(terms)

values = []

for i in terms:
    if i[0] not in "+-":    # no leading sign (only case should be first term +)
        values.append(int(i))
    elif i[0] == "-":       # negative term
        values.append(int(i[1:]) * -1)
    else:                   # only case should be positive terms (not first)
        values.append(int(i[1:]))

print(values)

result = sum(values)
print(result)