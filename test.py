from constraints import *
from arc_consistency import *
from solve import backtrack

x = Variable()
y = Variable()
z = Variable()

variables = [x, y, z]
constraints = [x >= 3*y + 1, z != y + 5]
domains = [{1,2,3,4,5}, {1,2,3,4}, {5,6}]
res = backtrack(variables, domains, constraints)
if (res):
    print(F"x = {x.evaluate()}")
    print(F"y = {y.evaluate()}")
    print(F"z = {z.evaluate()}")
else:
    print("Impossible problem")
