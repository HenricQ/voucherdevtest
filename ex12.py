def consumo(dist, lit):
    kmpl = dist / lit
    print(f"Consumo de {kmpl:.2f}km/l")
    if kmpl < 8:
        print("TÁ BEBENDO EM!!!!")
    elif kmpl < 15:
        print("O consumo está normal")
    else: 
        print("Está muito econômico!")


consumo(140, 18)    