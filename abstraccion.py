# en esta seccion de abstraccion, podemos observar como realizamos nuestra clase y establecemos su construcor junto a sus metodos
# desarrollaremos un automovil el cual debera ser capaz de encerderse y manejarse

class Automovil(): # creamos nuestra clase "Objeto"
    def __init__(self) -> None:
        self._estado = "apagado"
    
    def encender(self): # creamos su metodo"accion" de encender
        self._estado = "encendido"  
        print("El auto esta encendido")
        
    def conducir(self): # creamos su metodo"accion" de manejar, pero:
        if self._estado == "apagado":
            self.encender() # usamos la condicional if para poder validar que si esta apagado, ejecutamos le motodo de encender al encerderse se proda manejar
        print("Manejando")
        
mi_auto = Automovil() # instanciamos la clase"creamos nuestro objeto"
mi_auto.conducir()# llamamos al metodo conducir y listo

# hemos de enfatizar que lo que busca la abstraccion es separar lo complejo del codigo con la sencilles de su uso, mejor dicho
# al crear nuestra clase sus atributos y metodos, estamos creando una complejidad en el codigo que necesitrar que se cumplan para ejecutar la accion de conducir
# pero el usuario directamente no vera eso, simplemete ejecutrar la accion y esta se realizara, dandonos a entender que todo el codigo con el proceso para que nuestro
# automovil ande se resume en una accion que ejecuta el usuario y esta por ende debe de realizarce, sin que el usuario vea todo el codugo en funcionamiento detras de dicha accion
# es decir abstraemos el codigo 