def brackets_are_valid(expr: str) -> bool:
    ret = False
    stack = []
    last_open_bracket_pos = 0

    for i, c in enumerate(expr):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                last_open_bracket_pos = stack.pop()
            except IndexError:
                print(f"Closing bracket at {i} has no opening.")
                print(expr)
                print(" "*i + "^ here.")
                return False

    if len(stack) == 0:
        return True
    else:
        print(f"Open bracket at {last_open_bracket_pos} has no closing.")
        print(expr)
        print(" "*last_open_bracket_pos + "^ here.")
        return False