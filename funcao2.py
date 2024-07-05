from random import choice

def hello(nome = 'desconhecido'):
    emojis = ['😎😍😥😆', '😋🙄🤯😱', '😱😳🥰👽', '👽👾🤓🥴', '😴🤨🤩🙂']
    print(f"Seja bem vindo {nome} {choice(emojis)}")


hello("João")
hello("Robert")
hello("Victor")
hello("Henrico")
hello("Carlinhos")