# Principio de abierto y cerrado, este principio no dice que nuestro codigo debe estar implementado para dos acciones, abierta a funciones de escalabilidad
# o mejor dicho abierta a nuevas funcionalidades, pero cerrado a su modificacion, es decir podemos extender el codigo hacerlo mas escalable y mas eficaz
# pero el mismo debe estar cerrado para ser modificado es decir que no se deba tocar la clase padre los modulos principales entre otros

# ahora veremos un ejemplo de esto mismo

class notificador(): # clase padre la cual haremos que de su herencia a las demas funciones
    def __init__(self,usuario,mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
# funciones hijas para que cumplan su principal rol usando los atributos de las funciones Padre
class NotificadorEmail(notificador): # haremos que herede de "notificador"
    def notificar(self):
        print(f"Enviando MAIL a {self.usuario.email}") # al heredar de la clase padre podemos hacer que cumpla el metodo indicado con el mensaje que queramos realizar
        
class NotificadorSMS(notificador): # haremos que herede de "notificador"
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}") # igual para los demas metodos solo que para entidades distintas es decir ya sea por formato SMS

class NotificadorWhatsApp(notificador): # haremos que herede de "notificador"
    def notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.whatsapp}") # formato WhatsApp

class NotificadorX(notificador): # haremos que herede de "notificador"
    def notificar(self):
        print(f"Enviando X a {self.usuario.x}") # Formato X
        
# y esto nos deja con un codigo el cual escala con mas funcionalidades queramos agergarle pero no para modificar la clase padre la cual nos permite escalar dicho codigo
# de igual manera esto se convierte en un codigo con buena practica

# en general la clase notificador nunca se modifico en todo el codigo, solo se crearon subclases heredando de dicha clase para poder crear funcionamiento a partir de esta
# pero la clase principal nunca se modifico