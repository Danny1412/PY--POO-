# Principio de segregacion de la interfaz, En este principio nos indica que debemos ser capaces al momento de realizar una clase abstracta con el sentido de plantilla
# o el de una clase con sus funcionamientos, la cual nos permita poder realizar cada de sus metodos sin la necesidad de los demas, ya que solo requerimos de una interfaz
# a la subclase que debamos trabajar

from abc import ABC, abstractmethod

# esta es la manera correcta de establecer nuestras clases y metodos abstractos para el uso de cada metodo en nuestras proximas subclases
class Trabajador(ABC):
    @abstractmethod
    def trabaja(self):
        pass
    
class Dormilon(ABC):
    @abstractmethod
    def duerme(self):
        pass
    
class Comelon(ABC):
    @abstractmethod
    def come(self):
        pass
# aca tenemos nuestras clases abtractas con dichos metodos abtractos que cumpliran las funciones que necesitemos en sus siguienes subclases

class Humano(Trabajador,Dormilon,Comelon): # creamos nuestra clase humano y le heredamos nuestras clases abstractas para su uso
    def come(self):
        print("El humano come")
        
    def duerme(self):
        print("El humano duerme")
        
    def trabaja(self):
        print("El humano trabaja")
# definimos el uso de cada clase y la misma se cumplira ya que usa cada metodo de cada clase dependiendo de la clase que estemos implementando en este caso un humano
        
class Robot(Trabajador): # luego en nuestra clase robot tenemos que este al ser una maquina no necesita funciones basicas como comer o dormi ya que no esta hecho para eso
    def trabaja(self):
        print("El robot esta trabajando") # en ese caso le heredamos de la clase trabajador y cumplira dicho metodo ya que es el unico heredado
        
# y asi segregamos interfazes mejor explicado como, usamos ciertas clases para las subclases a crear y con que objetivos las creamos, como robot es solo una maquina puede trabajar indefinidamente
# mientras que el humano al ser una ser viviente si requiere las demas funciones basicas, dando por hecho que no perdemos espacio en lineas ni codigo de relleno al usar cada clase para cada subclase con metodos abstractos

robot = Robot()

humano = Humano()

robot.trabaja()

humano.trabaja()
humano.duerme()
humano.come()