class Persona():
    def __init__(self,nombre,edad,peso) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def __str__(self): 
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self): 
        return f'Persona("{self.nombre}",{self.edad})' 

# en este apartado veremos un metodo para operadores aritmeticas, y usaremos la suma, esto definira que sucedera con todos los objetos a la hora de sumarse

    def __add__(self,otro):# aca creamos nuestro metodo y lo que haremos es asignarle un atributo para implementarlo en la operacion
        nuevo_valor = self.edad + otro.edad # creamos la variable que almacenara dicha operacion y luego
        nuevo = self.peso + otro.peso
        return Persona(self.nombre+otro.nombre,nuevo_valor,nuevo) # retornaremos el resultado en la calse Persona con los atributos de los nombres y todo se almacenara el "nuevo_valor"
# sinedo que el retorno debe estar anclado con las variables y el codigo que cumplan, es decir que sumen cada atributo que este creado en la clase
        
dalto = Persona("Lucas",21,30.0) 
pedro = Persona("Pedro",30,25.1)
maria = Persona("Maria",18,25.2)

nueva_persona = pedro + dalto + maria
print(nueva_persona.peso)