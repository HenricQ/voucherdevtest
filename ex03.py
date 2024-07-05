def negcheck(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
    

print(negcheck(6))
print(negcheck(-16))
print(negcheck(0))