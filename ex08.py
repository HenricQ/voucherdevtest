def media(n1, n2, n3, md = 'a'):
    if md.upper() == 'A':
        return (n1 + n2 + n3) / 3
    elif md.upper() == 'P':
        return (n1*5 + n2*3 + n3*2) / 10
    

print(media(8, 7, 10))
print(media(8, 7.4, 6, 'p'))