class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def imprimirRaio(self):
        print(f"O raio do círculo é {self.raio}")

    def calcularArea(self):
        print(f"A área do círculo é de {3.1415 * self.raio**2}")

    def calcularCircunferencia(self):
        print(f"A circunferência do círculo é de {2 * self.raio * 3.1415}")