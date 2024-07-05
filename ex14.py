from random import shuffle, choice

def embaralha(p):
    ord = []
    for i in range(len(p)):
        ord.append(i)
    shuffle(ord)
    s = ''
    for i in ord:
        g = choice((0 ,1))
        if g == 0:
            s += p[i].upper()
        elif g == 1:
            s += p[i].lower()
    return(s)



print(embaralha('python é muito divertido'))