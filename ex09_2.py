def calcEstac(minutos): 
    valor = 0
    if minutos > 15:
        horas = (minutos // 60)
        if horas <= 1:
            valor = 9
        else:
            horas -= 1
            valor = horas * 1.5 + 9
    pis = valor * 0.0033
    print(f"PIS : R${pis:.2f}")
    cofins = valor * 0.002
    print(f"COFINS : R${cofins:.2f}")
    icms = valor * 0.17
    print(f"ICMS : R${icms:.2f}")
    print(f"{minutos} minutos, valor do estacionamento: R${valor + pis + cofins + icms:.2f}\n")
        

calcEstac(240)

        