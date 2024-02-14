# principio de inversion de dependencias, nos dice que nuestras modulos y metodos, no pueden estar ligados del mas grande al mas pequeño 
# sino el pequeño al mas grande, ya que si una clase tiene que cumplir una funcion mas importante por ende requiere muchas mas cosas, no va a tener que depender
# de una clase menor la cual solo da soporte para una de sus cuantas funciones

# este codigo es romper el principio de inversion de dependencias
# class Diccionario(): # clase pequeña 
#     def verificar_palabras(self,palabra):
#         #logica para verificar palabras
#         pass
    
# class CorrectorOrtografico(): # clase grande
#     def __init__(self) -> None:
#         self.diccionario = Diccionario()
        
#     def corregirtexto(self,texto):
#         #usamos el diccionario para corregir el texto

# para usar correctamente este principio, usaremos una clase abstracta  
from abc import ABC, abstractmethod

class verificadorortografico(ABC): # creando nuestra calse para verificar la ortografia haremos lo siguiente
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(verificadorortografico): # le heredaremos dicha clase a nuestra clase diccionario
    def verificar_palabra(self, palabra): # el cual poseera el metodo para verificar las palabras de nuestra clase padre
        # logica para verificar palabra si esta en el diccionario
        pass

class Servicioweb(verificadorortografico): # y aca tenemos otra clase la cual verifica la palabra pero de distinta manera que el diccionario
    def verificar_palabra(self, palabra): # y asi nuesrtro codigo es mas escalable usando distintas interfaces y no dependemo de un pequeño metodo o clase
# para hacer todo la funcion importante del codigo
        # logica para verificar palabra mediante una web
        pass
        
class Corrector_Ortografico(): # luego crearemos  nuestro corrector es decir la funcion mas importante ya que este realizara todo lo que usuario le pida
    def __init__(self,verificador) -> None: # definimos su construccion 
        self.verificador = verificador
    
    def corregir_texto(self): # luego usamos un metodo para corregir el texto que necesitemos
        # usamos el verificador para corregir el texto
        pass
    
corrector = Corrector_Ortografico(Servicioweb())

# lo que podemos destacar de aca que la funcion mas importante "Corrector_Ortografico", usa como base el verificador para el texto
# pero este no depende de dicho correcto(metodo), y que si necesitamos cambiar algo de nuestro verificador ortografico el cual por los momentos es "Diccionario"
# no pasaria nada ya que podemos muchisimos otros metodos mas que necesitemos definir ya sea por un servicio Web o algun otro metodo desarrollo o a desarrollar
# es decir no dependemos de un solo metodo no dependemos de nada, solo nos manejamos con una interfaz de muchas mas a las que podamos acceder 