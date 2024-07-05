def soma(num1, num2):
    sum = num1 + num2
    return sum


def tabuada(num = 0):
    j = 11
    if num > 10:
        j = num + 1 
    for i in range(1, j):
        print(f"{num} * {i} = {num * i}")


tabuada(int(input("Digite um número inteiro: ")))