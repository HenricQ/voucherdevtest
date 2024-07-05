from random import randint

def sorteia(n):
    res = []
    for i in range(n):
        res.append(randint(0,60))
    return res

def somaPar(l):
    s = 0
    for i in l:
        if i % 2 ==0:
            s += i
    return(s)


numeros = sorteia(5)
print(somaPar(numeros))