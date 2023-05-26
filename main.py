def solve(problem: str):
    problem = problem.replace(" ","") # 10*20
    operations: list = ["*", "+", "-", "/"]
    for operation in operations: # operation = *
        if operation in problem:
            x, y = problem.split(operation) # 10,20
            x, y = float(x), float(y)
            op = operation
            break
    if   op == "*": print(x * y)
    elif op == "+": print(x + y)
    elif op == "-": print(x - y)
    elif op == "/": print(x / y)