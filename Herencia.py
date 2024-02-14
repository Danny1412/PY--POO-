# en esta clase vemos la herencia simple y jerarquica,
# la herencia simple es cuando heredamos de una superclase a una subclase, ya que como podemos ver a continuacion
class Persona(): # tenemos la clase persona
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self ):
        print("Estoy hablando")
# en esta clase tenemos sus atributos y un metodo

class Empleado(Persona): # luego definimos nuestra subclase empleado, heredando todo los atribuos y metodos de persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): 
        super().__init__(nombre, edad, nacionalidad) # en esta seccion "super", es donde declaramos el constructor interno donde van los atributos heredados de la clase Persona
        self.trabajo = trabajo
        self.salario = salario
# con los self establecemos los atributos nuevos "trabajo" y "salario"

# aca creamos otra clase heredamos lo mismo de "Persona", pero con la diferencia de que aca establecemos otros atributos diferentes
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)    
        self.notas = notas
        self.universidad = universidad
# ahora podemos ver que esto es una herencia jerarquica

# aca establecemos los atributos de cada clase 
daniel = Empleado("Daniel", 52, "veneco","Programador",100000)

daniel.hablar() #aca usamos sus metodos 