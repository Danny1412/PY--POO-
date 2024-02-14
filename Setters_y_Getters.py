# los setters y los getters son modelos implementados para entender como validamos la seguridad de las propiedades es decir:
# que si tenemos archivos "privados" o "muy privados", tendremos distntas forams de reconocerlo y entenderlo como veremos

class Persona():
    def __init__(self,nombre,edad) -> None:
        self.__nombre = nombre # aca el "__" nos indica que es muy privado y si intentamos acceder a el de la manera convencional no nos dejara
        self.__edad = edad

# aca entra getter que es cuando lo declaramos, es decir creamos una funcion(metodo), el cual usaremos para validar que se puede acceder a __nombre

    def get_nombre(self):
        return self.__nombre # retornaremos su valor y lo haremos ver en pantalla, ¿como?, facil primero instanciamos la clase y luego la imprimimos llamando a nuestro metodo
    
# ahora tenemos a setter, que es cuando le damos un valor a dicha propiedad, es decir podremos reemplazar el valor original de nuestra propiedad "muy privada"
    
    def set_nombre(self, new_nombre): # lo que haremos es establecer nuestra nueva propiedad
         self.__nombre = new_nombre # entonces establecer que __nombre, almacene lo que le pasemos a nuestra nueva propiedad
    
dalto = Persona("Dalto",21) # instancia de la clase

# uso de setter(set)
dalto.set_nombre("Pepa") # aca establecemos nuestra nueva propiedad con setter y luego llamamos a getter para obtener el valor pero de nuestra propiedad

# uso de getter(get)
nombre = dalto.get_nombre()
print(nombre)

