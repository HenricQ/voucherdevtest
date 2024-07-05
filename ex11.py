def pot(b, e):
    r = 1
    for i in range(e):
        r *= b
    return r

print(pot(2,8))