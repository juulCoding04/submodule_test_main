def return_calc(n1, n2, operation):
    if operation == 'sum':
        return int(n1)+int(n2)
    elif operation == 'subtract':
        return int(n1)-int(n2)
    elif operation == 'divide':
        return int(n1)/int(n2)
    elif operation == 'multiply':
        return int(n1)*int(n2)
    else:
        return 'invalid operation'