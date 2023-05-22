from constraints import *
from solve import backtrack

def queens(n):
    """
    Solve the n queens problem
    """

    variables = [Variable() for _ in range(n)]              # the positions of the queens (row id)
    domains = [{i for i in range(1, n+1)} for _ in range(n)]  # can take any row as value
    constraints = []
    for i in range(n):
        for j in range(i+1, n):
            diff = j - i
            pos1 = variables[i]
            pos2 = variables[j]
            constraints.append(pos1 != pos2)
            constraints.append(pos1 != pos2 - diff)
            constraints.append(pos1 != pos2 + diff)

    res = backtrack(variables, domains, constraints, inference=False)
    if res:
        return variables
    return None

if __name__ == "__main__":
    n = 8
    res = queens(n)

    if res != None:
        for i in range(len(res)):
            var = res[i]
            print(F"Queen on column {i+1} should be placed in row {var.evaluate()}")
    else:
        print("Impossible problem")