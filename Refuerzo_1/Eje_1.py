# creamos la clase
class Persona():
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        print(f"""
              Su nombre es: {self.nombre}
              Su edad es: {self.edad}
              Su DNI es: {self.dni}
              """)
    
    def esmayordeedad(self):
        if (self.edad >= 18):
            print(f"La persona es mayor de edad: {self.edad}")
        else:
            print(f"La persona no es mayor de edad: {self.edad}")

Pedro = Persona("Pedro",18,"30.982.082")



Pedro.esmayordeedad()