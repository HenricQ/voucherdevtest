def opr(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '/':
        return n1 / n2
    elif op == '*':
        return n1 * n2
    else:
        return 'erro'
    

print(opr(6, 5, '+'))
print(opr(6, 5, '*'))