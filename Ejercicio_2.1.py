# Cuando hereda, hereda todo lo que esta en la clase, es decir la clase hijo siempre va a heredar todo lo que se cree en la clase padre
# asi todas las demas clases tendras sus metodos y se ejecutaran en la clase que se le herede al llamar a sus metodos

class Animal():
    def comer(self):
        print("Esta comiendo")
  
class Mamifero(Animal):
    def amamantar(self):
        print("Esta amamantando")
    
class Ave(Animal):
    def volar(self):
        print("Esta volando")
        
class Murcielago(Mamifero, Ave):
    pass
        
m = Murcielago()

m.comer()
m.volar()
m.amamantar()
