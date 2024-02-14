# aca veremos como funciona el encapsulamiento, es decir veremos como exiten atributos metodos a los cuales el desarrollador
# no puede acceder y tendra que hacerñp de distinta forma, para esto haremos lo siguiente 

class Clase():
    def __init__(self) -> None:
        self.__atributo_privado = "Valor" # al cear el atributo "privado" se debe colocar dos guiones bajos "__" y el nombre o denominacion del atributo
        
    def __Hablar(self): # en el caso de los metodos es lo mismo que los atributos
        print("Hola guapo")
        
objeto = Clase() # realizamos lo normal con nuestras clases

print(objeto.__Hablar()) # y por ultimo intentamos llamar a nuestro metodo o atributo, con un resultado erroneo ya que el desarrollador no puede acceder

# normalmente el encapsulamiento ayuda a comprender y entender mejor el codigo a la hora de un desarrollo mas complejo

