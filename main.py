import math

n1 = input('number 1: ')
n2 = input('number 2: ')
operation = input('sum/subtract/divide/multiply:')

if operation == 'sum':
    print(n1+n2)
elif operation == 'subtract':
    print(n1 - n2)
elif operation == 'divide':
    print(n1/n2)
elif operation == 'multiply':
    print(n1*n2)
else:
    print('invalid operation')