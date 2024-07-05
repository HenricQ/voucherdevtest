def criaMatrizUser(ns):
    mat = []
    for i in range(4):
        lin = []
        for j in range(4):
            n = int(input(f"Digite um número para index [{i},{j}]: "))
            lin.append(n)
        mat.append(lin)
    for i in mat:
        print(i)
    if ns > 3:
        ns = 3
    print(f"A soma da linha [{ns}] da matriz é: {sum(mat[ns])}")

criaMatrizUser(2)