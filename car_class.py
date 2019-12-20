class Car:
    
    year = 0
    
    def __init__(self, motore, peso, prezzo):
        self.motore = motore
        self.peso = peso
        self.prezzo = prezzo
    
    def old(self):
        self.year += 1
        self.prezzo -= 100
    
    def costum(self):
        self.motore += 100
        self.peso -= 300
    
    


bmw = Car(567, 1789, 10000)
