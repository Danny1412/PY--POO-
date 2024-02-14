# aca veremos los metodos especiales los cuales son aquellos que inician con "__" y finalizan con "__"

class Persona():
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self): # este metodo transforma la representacion de la clase a un string
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self): # este metodo realiza lo mismo que "__str__", solo que lo usa para representar al objeto
        return f'Persona("{self.nombre}",{self.edad})' # en mejores palabraas estructuramos nuestros valores a retornar sin las variables

    
dalto = Persona("Lucas",21) # instancionamos nuestra clase

reper = repr(dalto) # aca representamos la clase es decir la clase "Persona" tiene una "tupla", con los valores de "Lucas" y 21, es decir una representacion para reconstruir el objeto
result = eval(reper) # aca es el metodo repr pero ya instanciado es decir ya tenemos el objeto en su totalidad, y aca ya estaria nuestro objeto recontruido almacenado en "result"

print(result.edad) # podemos llamar cualquiera de los atributos porque tenemos al objeto en su total instancia