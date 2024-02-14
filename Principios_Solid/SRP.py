# Principio de responsabilidad unica, nos indica que cada clase se encarga de una funcion especifica como el ejemplo que veremos
# el ejemplo que usaremos es el mover un auto lo cual lleva bastantes implicaciones, pero veremos dos implicaciones nada mas

# primero creamos un tanque de gasolina el cual se encargara de su combustible, cuanto combustible posee y cuanto combustible usara 
class TanqueGasolina():
    def __init__(self) -> None:
        self.combustible = 100 # cantidad total de combustible

    def agregar_combustible(self,cantidad): # metodo para agregar pero no lo usaremos, es por si deseamos agregarle mas es decir escalamos el codigo
        self.combustible += cantidad
    
    def obtener_combustible(self): # esto es considera un getter, pero es un metodo para saber cuanto combustible tiene es decir accedemos a su cantidad
        return self.combustible
    
    def usar_combustible(self,cantidad): # luego el metodo para usar el combustible del tanque cuando el auto se mueva
        self.combustible -= cantidad
# como vemos el TanqueGasolina, se encarga de la administracion de combustible, pero sabemos que necesitamos que el carro se mueva, para eso haremos lo siguiente

# creamos la clase auto y le daremos todas las funciones para que este pueda moverse, pero con que se movera, claro con el tanque de gasolina y su combustible
class Auto():
    def __init__(self,tanque) -> None: # instanciamos el tanque sabiendo que este se crea con el requisito de la primera clase
        self.posicion = 0 # creamos un valor estatico sabiendo que este debe es parte del movimiento
        self.tanque = tanque # instanciamos dicho valor pasado como parametro
        
    def mover(self, distancia): # luego crearemos nuestro metodo de mover el cual tendra la distancia y cumplira lo siguiente
# con una condicional haremos nuestro movimineto teniendo en cuenta que
        if self.tanque.obtener_combustible() >= distancia / 2: # si el tanque(el cual accede a la cantidad de combustible de "TanqueGasolina", debe ser mayor a la distancia recorrida entre dos, es decir la mitad)
            self.posicion += distancia # luego vaidamos esto, como la posicion incial es 0 le sumaremos lo que nuestra validacion tenga
            self.tanque.usar_combustible(distancia / 2) # luego debemos restarle al tanque ya que este tiene un limite de 100 y este debe irse consumiendo, accediendo a la validacion veremos cuanto hay que restar
# esto se resta ya que usamos nuestro valor de tanque junto con el metodo de "usar_combustible"
            print("moviste el auto") # daremos visto bueno de que dicho auto se movio
        else:
            print("no hay suficiente combustible") # al momento de no avanzar mas cortaremos dicho movimiento 
            
    def posici(self): # luego creamos un getter o funcion el cual nos permita ver la posicion avanzada
        return self.posicion
    
tanque = TanqueGasolina() # insanciamos nuestro tanque
auto = Auto(tanque) # luego nuestro auto, pero al auto le pasaremos nuestro objeto de tanque para que lo pueda usar

# aca realizamos todas las acciones requeridas para ver el funcionamiento de nuestras dos clases
print(auto.posici())
auto.mover(10) # aca hay que pasarle cuanto queremos que se mueva es decir la distancia
print(auto.posici())
auto.mover(20)
print(auto.posici())
auto.mover(60)
print(auto.posici())
auto.mover(100)
print(auto.posici())
auto.mover(100)
print(auto.posici())
# al llegar al limite veremos que ya no puede quitar mas del tanque el cual no tiene suficiente combustible para moverse, finalmente devolviendonos la posicion en la cual quedo
