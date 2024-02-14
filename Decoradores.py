# aca veremos el concepto de decoradores, el cual se rige por ser como su nombre lo indica, decora el codigo de una funcion, mas no interviene ni alterada nada sobre el
# como veremos a continuacion

def decorador(funcion): # creamos la funcion decoradora, la cual tendra su parametro de "funcion"
    def funcion_modificada(): # aca creando otra funcion podemos iniciar  lo que vaya antes del codigo de nuestra funcion
        print("Antes de llamar funcion")
        funcion()
# en este espacio puede ir lo que se ejecute despues del codigo es decir lo que va despues de la funcion que llamemos
    return funcion_modificada # retornamos todos los valores

# en el siguiente codigo creamos nuestra funcion y llamamos a nuestro decorador pero no es la mejor opcion

# def saludo():
#     print("Hola Dalto")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

# la mejor opcion es la que se realiza aca abajo

@decorador # llamamos nuestra funcion decorador que nos mostrara las primeras funciones creadas
def saludo(): # funcion que se utilizaremos como funcion de uso
    print("Hola Dalto")
    
saludo() # llamamos a la funcion y eso seria todo

# como el decorador solo agrega eso decoraciones a nuestro codigo para hacerlo mas estandar y comprensible 