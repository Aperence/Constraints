from constraints import *
from arc_consistency import *

x = Variable()
y = Variable()
z = Variable()

constraints = [x >= 2*y + 1, z != y + 4]
domains = [{1,2,3,4,5}, {1,2,3,4}, {5,6}]
print(arc_consistency([x, y, z], domains, constraints))
