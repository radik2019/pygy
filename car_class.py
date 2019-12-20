class Car:
    
    year = 0
    
    def __init__(self, motore, peso, prezzo):
        self.motore = motore
        self.peso = peso
        self.prezzo = prezzo
    
    def old(self):
        self.year += 1
        self.prezzo -= 100
    
    def price(self):
        pass



bmw = Car(600, 1600, 1000)
audi = Car(587, 1200, 1000)
mercedes = Car(598, 1455, 1000)

alfa = Car(656, 1100, 1000)
ford = Car(788, 2000, 1000)
