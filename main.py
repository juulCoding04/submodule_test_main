import math
import submodule_test_1.math_tooling.return_calc as rc

n1 = input('number 1: ')
n2 = input('number 2: ')
operation = input('sum/subtract/divide/multiply:')

calc = rc.return_calc(n1, n2, operation)
print(calc)