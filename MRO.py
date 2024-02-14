# el MRO, toma como secuencia los ordenes que le da python a las clases y su centenido

class A: # Una vez encontrado nuestro metodo "Hablar", se ejecutara, porque saltamos de B a C y no directamente de B a A y cerrar de una vez
# bueno esto es porque la prioridad en python es comprobar todas las clases existentes asi una sea mas corta que otra
# Al ver que B no contiene anda, iremos a C, ya que en la clase D no tenemos ningun salto hacia A, si B no lo tiene ira a C que es su segunda clase
# recorrera todo el camino de C hastar con el metodo
    def hablar(self):
        print("Hola desde A")

class B(A): # Una vez aca buscaremos el metood hablar, como lo encontramos iremos a nuestra siguiene ruta C, porque?, simple B es la ruta mas corta y con un final directo
# pero porque no finaliza recordemos que tenemos a la clase F heredando de A, asi que iremos a nuestro punto de partida para ver nuestra proxima ruta C
    def hablar(self):
        print("Hola desde B")
        
class F(A): # Aca vendremos buscando el metodo "Hablar", ya que no se encuentra aca iremos a nuestra siguiente clase,  A
    def hablar(self):
        print("Hola desde F")

class C(F): # ya recorrido B venimos a C, buscando el motodo llamado "Hablar", como aca no esa iremos a la siguiente clase F
    def hablar(self):
        print("Hola desde C")
        
class D(B,C): # desde aca inician nuesras rutas, B y C, una vez recorrida la primera, vamos a la segunda
    def hablar(self):
        print("Hola desde D")
        
d = D()

F.hablar(d) # Con esta manera de llamar al metodo dentro de nuestra clase lo hacemos siguiendo el orden de, a la variable "d", le pasamos como valor la "class D"
# luego queremos llamar al metodo de la clase mas arriba la "class F", entonces llamamos al metodo hablar de la clase F con "F.hablar()"
# pero aca lo que haremos es pasarle a nuestro metodo, nuestra variable con nuestra clase asignada es decir "F.hablar(d)" y con eso accedemos al valor de mas arriba
# con el valor de mas abajo 

#print(D.__mro__)


# el MRO, es el orden que usa python entre metodos y clases, mayormente con las herencias

# class Persona(): 
#     def __init__(self, nombre, edad, nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad
        
# class Artista():
#     def __init__(self,habilidad):
#         self.habilidad = habilidad
    
#     def mostrar_habilidad(self):
#         return f"Mi habilidad es: {self.habilidad}"
        
# # En esta clase denominada "EmpleadoArtista", podemos observar los atrivutos de la clase Persona, y de la clase Artista
# class EmpleadoArtista(Persona,Artista):
#     def __init__(self,nombre, edad,nacionalidad,habilidad,puesto,salario): # aca en el constructor le agregamos los atributos sacados de las dos clases anteriores
#         Persona.__init__(self,nombre,edad,nacionalidad) # luego validamos esos atributos creado las clases dentro de nuetro contructor "como ejemplo tenemos "Super""
#         Artista.__init__(self,habilidad)
#         self.salario = salario # luego declaramos nuestros atributos creados para la clase EmpleadoArtista
#         self.empresa = puesto  
        
#     def presentarse(self):
#         print(f'Hola soy {self.nombre} mi habilidad es: {self.mostrar_habilidad()}, trabajo de {self.empresa}') # aca usamos super ya que la diferencia entre self y super, es que self accede al metodo reescrito previamente, es decir si escribimos un metodo con el mismo nombre pero que ejecute otro codigo accederemos a ese
# # mientras que con super, accedemos al metodo de la clase padre es decir de artista ya que super accede al metodo escrito en la clase, cual clase tiene este metodo si "Artista"
        
# roberto = Artista("Cantar")