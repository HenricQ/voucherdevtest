def trangulo(n, c='*'):
    for i in range(1,1+n):
        print(c*i,end='')
        print()
    for i in range(n-1,0,-1):
        print(c*i,end='')
        print()


trangulo(6, 'aa')