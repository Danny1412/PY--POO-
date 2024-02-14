# Al crearse la clase celular, desarrollamos una funcion la cual se convierte en un "metodo especial"
# El cual se va a ejecuar automaticamente y de tal manera realizar cada proceso que se le
class Celular:
    def __init__(self, marca, modelo, camara): # aca estableciendo el constructor "init", debemos establecer en los parametros "self", para hacer referencia al uso principal del metodo
# luego de establecer self, damos los parametros  los cuales seran los acompañantes de dicho objeto
        self.marca = marca 
        self.modelo = modelo # aca self.modelo = modelo, es para pasarle el valor, establecemos dentro de nuestro contructoraa, como queremos que se llame "self.modelo", y va almacenar el valor que queremos otorgarle "modelo", valor el cual se usara en una variable mas adelante
        self.camara = camara
        
# luego de todo el proceso establecemos los argumentos de los parametros almacenados en una varaible, donde llamaremos a la clase y seguido establecemos los valores de los parametros
# aqui es donde se le entregan los atributos a nuestro objeto, es decir le pasamos los valores los cuales  lo van a identificar 
celular1 = Celular ("Samsumg", "S23", "48MP")
celular2 = Celular ("Apple", "Iphone 15 Pro", "96MP")

# y luego podemos mostrar en pantalla, el atributo que queremos conocer del objeto, es decir
# tenemos dos celulares y queremos saber el modelo del celular uno y la camara del celulas dos

print(f"El modelo del primer celular es: {celular1.modelo}, la camara del segundo celular es: {celular2.camara}")

# El parametro de Self, hace referencia al mismo objeto es decir la clase, como tenemos clase "Celular", Self como parametro en Def, hace referencia a nuestra clase
# que mejor dicho es nuestro "Objeto"