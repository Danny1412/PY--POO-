class Persona(): 
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
# En esta clase denominada "EmpleadoArtista", podemos observar los atrivutos de la clase Persona, y de la clase Artista
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre, edad,nacionalidad,habilidad,puesto,salario): # aca en el constructor le agregamos los atributos sacados de las dos clases anteriores
        Persona.__init__(self,nombre,edad,nacionalidad) # luego validamos esos atributos creado las clases dentro de nuetro contructor "como ejemplo tenemos "Super""
        Artista.__init__(self,habilidad)
        self.salario = salario # luego declaramos nuestros atributos creados para la clase EmpleadoArtista
        self.empresa = puesto  
        
    def presentarse(self):
        print(f'Hola soy {self.nombre} mi habilidad es: {self.mostrar_habilidad()}, trabajo de {self.empresa}') # aca usamos super ya que la diferencia entre self y super, es que self accede al metodo reescrito previamente, es decir si escribimos un metodo con el mismo nombre pero que ejecute otro codigo accederemos a ese
# mientras que con super, accedemos al metodo de la clase padre es decir de artista ya que super accede al metodo escrito en la clase, cual clase tiene este metodo si "Artista"
        
roberto = Artista("Cantar")

herencia = issubclass(EmpleadoArtista,Artista)# con el metodo de "issubclass", podemos definir si una es una subclase del otro es decir primero ponemos la clase general, y luego su subclase liego al llevar esto a pantalla nos dira si es verdadero o falso
instancia = isinstance(roberto,Artista) # luego veremos si la instancia pertenece a la clase, es decir si nuestro objeto pertenece a la clase a la que preguntamos, luego nos dira si es verdadero o falso

print(instancia)

# y con todo lo acabado de ver, se reconoce como herencia multiple