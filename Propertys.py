# aca veremos el uso de Propiedades o mejor dicho el correcto uso de setter y getter de la anterior clase
# en la anterior clase vimos setter y getter y ahora veremos su correcto uso con la implementacion de Python o mejor dicho como originariamente son de python

class Persona(): # empezamos con nuestra clase y nuestro atributo "muy privado"
    def __init__(self,nombre,edad) -> None:
        self.__nombre = nombre  
        self._edad = edad
# como en la anterior clase creamos getter se transformara en
    @property # este decorador que vemos aca, "@property" es getter y el lenguaje lo reconoce automaticamente 
    def nombre(self):
        return self.__nombre # establecemos lo que queremos retornar es decir el valor

    @nombre.setter # luego tenemos como bien es setter para modificar el valor de nuestro getter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre   
    
    @nombre.deleter # esta es una nueva implementacion que nos sirve para "eliminar" el valor en cuestion
    def nombre(self):
        self.__nombre
# es importante enfatizar que estos como bien se denominan "Decoradores", no afectan en si a la clase y su funcionamiento principal, solo para realizar implementaciones en el codigo
    
dalto = Persona("Dalto",21) # instanciamos la clase

nombre = dalto.nombre # aca llamos a get
print(nombre)

dalto.nombre = "Pepe" # aca llamamos a setter

nombre = dalto.nombre # aca reimprimimos el valor pero ahora con el valor de setter
print(nombre)

del dalto.nombre # aca borramos el nombre 

print("que haces maquina") # y como todo el codigo debe de funcionar tranquilamente siempre y cuando cada decorador o mejor dicho todo el codigo este en orden