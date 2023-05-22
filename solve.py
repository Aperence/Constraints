from arc_consistency import *
from constraints import *

def mvr(domains):
    idx = 0
    size = len(domains[0])
    for i in range(len(domains)):
        domain = domains[i]
        if len(domain) < size:
            size = len(domain)
            idx = i

    return idx

def backtrack(variables, domains, constraints, inference=True):
    """
    Return true if assignment found, results are stored in variables
    """
    if (len(variables) == 0):
        for constraint in constraints:
            if not constraint.evaluate():
                return False
        return True
    
    if inference:
        restricted_domains = arc_consistency(variables, domains, constraints)
        domains = restricted_domains

    for domain in domains:
        if (len(domain) == 0):
            return False

    var_idx = mvr(domains)
    var = variables[var_idx]
    rem_var = variables[:var_idx] + variables[var_idx+1:]

    dom = domains[var_idx]
    rem_dom = domains[:var_idx] + domains[var_idx+1:]

    for value in dom:
        var.assign(value)
        res = backtrack(rem_var, rem_dom, constraints)
        if res:
            return True
        var.unassign()

    return False
