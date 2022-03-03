# resistor_calculator.py
# Cole Frauzel
# 2022-03-03

# Takes in a circuit of resistors and calculates the total resistance.
# The circuit can contain series and paralell elements.
# A in series with B is written as A+B, and likewise | for paralell.
# Brackets can be used to disambiguate. | takes precedence over +.

# Note: resistor values in whole numbers, no prefixes, no commas.
# Will implement SI prefix support soon.

import postfix_utils as pfu

precedence = {
    '+': 0, '|' : 1
}

def evaluate(expr: list, operators: dict) -> float:
    stack = []
    left_operand = 0
    right_operand = 0

    for i in expr:
        if i.isnumeric():
            stack.append(int(i))
            continue

        elif i in operators:
            r1 = stack.pop()
            r2 = stack.pop()
            
            match i:
                case '+':   # resistors in series
                    rt = r1 + r2
                case '|':   # resistors in paralell
                    rt = (r1 * r2) / (r1 + r2)

            stack.append(rt)
                
        else:
            print("Non numeric/opeator in expression?")
            break

    return stack[0]


expr = "100|100|100|100"

if not pfu.brackets_are_valid(expr):
    exit()
else:
    terms = pfu.split_into_terms(expr, precedence)
    pfx_terms = pfu.infix_to_postfix(terms, precedence)
    ans = evaluate(pfx_terms, precedence)

    for i in terms: print(i, end=' ')
    print()
    for i in pfx_terms: print(i, end=' ')
    print()
    print(ans)