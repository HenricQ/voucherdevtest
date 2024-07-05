def putamadre(n,c='*'):
    for i in range(1,1+n):
        print(' '*(n-i),c*i,end='')
        print(c*(i-1), end='')
        print()


putamadre(10)
