def rev(num):
    revN = ' '
    for i in reversed(str(num)):
        revN += i 
    return int(revN)


print(rev(127))