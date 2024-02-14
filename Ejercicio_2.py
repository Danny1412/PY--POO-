# creamos una clase padre la cual tiene sus metodos y atributos, luego a la clase hijo le heredamos sus todo lo de la clase padre
# y a la clase hijo le agregamos los atributos y metodos que necesite
# por ultimo instanciamos nuestra clase(objeto) con sus atributos y ejecutamos sus metodos(acciones)

class Persona():
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def Datos(self):
        print(f"Su nombre es: {self.nombre}")
        print(f"Su edad es: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self,nombre, edad, grado) -> None:
        super().__init__(nombre,edad)
        self.grado = grado
        
    def Grado(self):
        print(f"Su grado es: {self.grado}")
        
        
estudiante = Estudiante("Daniel",19,"8vo")

estudiante.Datos()
estudiante.Grado()