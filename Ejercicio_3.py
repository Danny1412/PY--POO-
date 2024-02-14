# en ese ejercicio usaremos lo aprendido en los metodos especiales para crear un programa que nos permita crear un personaje y fusinarlo con otro

class Personaje(): # creamos la clase 
    def __init__(self,nombre,fuerza,velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
# agregamos todos sus atributos
        
    def __repr__(self) -> str: # ahora con el metodo "repr" para representar el objeto 
        return f"{self.nombre}(Fuerza: {self.fuerza},Velocidad: {self.velocidad})" # diciendole que nos muestre cada uuna de las caracteristicas de nuestro pj
    
    def __add__(self,otro_pj): # ahora para crear el metodo de fusion usaremos el metodo "add", el cual nos permitira sumar cada uno de los objetos y darnos al nuevo pj fusionado
        # establecemos las variables a cumplir la suma de los objetos
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre # encargada de sumar los nombres
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34) # encargada de sumar la fuerza
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34) # encargada de sumar la velocidad
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad) # retornamos cada valor de cada nueva variable a la hora de sumar cada pj
# no olvidemos que estas sumas se hacen con los atributos de la clase

# creamos nuestros pj principales 
goku = Personaje("Goku",100,100)
vegetta = Personaje("Vegetta",99,99)
jiren = Personaje("Jiren",130,140)

# creamos la "fusion" o mejor dicho suma de nuestros pj´s para asi sumar sus estadisticas e incrementarlas
gogetta = goku+vegetta
jiretta = gogetta+jiren

# imprimimos en pantalla todo
print(jiretta)
print(gogetta)
print(goku)
print(vegetta)
print(jiren)

# FIN

# OJO REALIZAR EL PROGRAMA A FINALIZAR EL CURSO