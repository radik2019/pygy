class Car:
    
    year = 0
    
    def __init__(self, motore, peso):
        self.motore = motore
        self.peso = peso
    
    def old(self):
        self.year += 1



bmw = Car(600, 1600)
audi = Car(587, 1200)
mercedes = Car(598, 1455)

alfa = Car(656, 1100)
