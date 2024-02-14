# En esta seccion de clases abstractas debemos recalcar dos cosas, no es lo mismo crear una superclase y subclases, a crear una "plantilla" y sus subclases
# es decir creamos una clase abstracta para usar todos sus atributos y metodos en todas las subclases con todo lo que posea nuestra clase abstracta

from abc import ABC, abstractclassmethod # tomamos del modulo abc y lo importamos al modulo ABC, el cual tendra como clase un metodo de clase abstracta

class persona(ABC): # al crear nuestra clase persona y darle como herencia ABC provoca que todo lo que esta aca no salga ni se ejecute de ahi
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")
# explicando mejor lo del principio, se entiende que todos los atributos y metodos creados en esta clase no se instancian
# simplemente se usan en todas las subclases que veremos a continuacion, con la unica condicion de que si no se usa ningun atributo ni metodo en las demas subclases
# no se ejecutara nada del codigo
        
class estudiante(persona): # creamos a la subclase de estudiante y le heredamos de nuestra clase abstracta persona que llamaremos como "plantilla"
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
    
    def presentarse(self): # en este caso al dejar el metodo "presentarse" con la funcion de pass, le damos un nuevo valor al metodo cambiando el que ya tenia dejandolo en blanco
        pass
    
# al heredar de plantilla establecemos todos sus atributos y metodos debemos darle un uso a cada uno a menos que estos ya lo posean

class trabajador(persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")
# en esta subclase usamos lo mismo que en la primera y ahora las instanciamos

pedro = estudiante("pedrito",21,"masculino","programacion") # instaciamos a estudiante
dalto = trabajador("lucas",22,"masculino","programacion") # instanciamos a trabajador

pedro.presentarse() # usamos nuestros metodos
pedro.hacer_actividad() # usamos nuestros metodos

dalto.presentarse() # usamos nuestros metodos
dalto.hacer_actividad() # usamos nuestros metodos