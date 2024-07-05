def criaMatriz(l, c):
    ret = []
    for i in range(l+1):
        lin = []
        for i in range(c):
            lin.append(1)
        ret.append(lin)
    for i in ret:
        print(i)

criaMatriz(5,3)