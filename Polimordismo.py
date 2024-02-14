# en esta clase veremos como python al ser un leanguaje de tipado dinamico nos permie realizar polimorfismo de maneras mas interactivas y menos extensas como otros lenguajes
# como veremos a continuacion tenemos polimorfismo en diferentes teorias, pero engloba el concepto de polimorfismo

class Animal(): # aca creamos una clase padre "animal", se la pasaremos a nuestras demas clases para darles un polimorfismo de herencia a que se refiere
    def sonido(self): # a que tenemos el mismo metodo pero se deja omite, para que nuestras demas clases cumplan dicho metodo
        pass # OJO esto es referenciado a lenguajes como C++ o Java, ya que estos no son como python de tipado dinamico con metodo de Duck Typing

class Gato(Animal):
    def sonido(self): # tenemos un metodo que realiza su accion
        return "miau"
    
class Perro(Animal):
    def sonido(self): # aca igual pero como podemos ver ambos retornan acciones distintas
        return "guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

# instanciamos nuestras clases
gato = Gato() 
perro = Perro()

print(gato.sonido()) # mostramos la accion de nuestro objeto, y como podemos ver estamos usando un mismo metodo solo que se le atribuye a diferente objeto
# es decir gato realiza un sonido pero en la clase gato vemos que su sonido es "miau", y si ponemos perro el resultado es logico "guau"

hacer_sonido(gato)# aca usamos otra cuestion la cual es crear una funcion con el parametro animal, el animal va a realizar nuestro "sonido"(metodo), el cual
# tiene como argumento nuestro objeto de gato, el sonido a realizar es "miau", con perro "guau  "

# Plus: El Polimorfismo de sobrecarga es crear una clase y asignarle el mismo metodo, pero dicho metodo funcionara cuantos mas parametros se le agregue es decir
# el codigo que vemos acontinuacion es la sobrecarga de metodos 
    
# class lector():
#     def leer(self):
#         print("No tengo que leer")
        
#     def leer(self,Historias,Noticias):
#         self.his=Historias
#         self.noti=Noticias
#         print(f"Estoy leyendo {self.his}, y {self.noti}")
        
#     def leer(self,Calculo,Filosofia):
#         self.calc=Calculo
#         self.fis=Filosofia
#         print(f"Estoy leyendo {self.calc}, y {self.fis}")
