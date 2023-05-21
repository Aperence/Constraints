
def arc_single_help(variables, domains, constraint, index, values):
    if index >= len(variables):
        if (constraint.evaluate()):
            for i in range(len(variables)):
                var = variables[i]
                values[i].add(var.evaluate())
        return 
    
    for value in domains[index]:
        variables[index].assign(value)
        arc_single_help(variables, domains, constraint, index+1, values)
        variables[index].unassign()


def arc_single(variables, domains, constraint):
    revised_domains = [set() for _ in range(len(variables))]
    arc_single_help(variables, domains, constraint, 0, revised_domains)
    return revised_domains

def domains_eq(d1, d2):
    for i in range(len(d1)):
        if (d1[i] != d2[i]):
            return False
    return True

def arc_consistency(variables, domains, constraints):
    revised = True
    while revised:
        revised = False
        for constraint in constraints:
            revised_domains = arc_single(variables, domains, constraint)
            if not domains_eq(domains, revised_domains):
                domains = revised_domains
                revised = True
    return domains