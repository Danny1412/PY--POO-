class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca 
        self.modelo = modelo
        self.camrara = camara

# aca en Def llamar, realizamos un metodo "(accion), tambien conocido", donde debemos establecer "self" en su parametro para que la nuestra clase lo reconozca dentro de la misma
# es decir para que nuestro objeto celular reconozca la accion o metodo de llamar   
    def llamar(self):
        print(f"Estas llamando desde un: {self.modelo}")

# todo aplica de la misma manera con cortar, simplemente los reconocemos con self como parte de nuestra clase, y ya el resto queda a decision de como se este realizando dicho codigo    
    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")
 
celular1 = Celular ("Samsumg", "S23", "48MP")
celular2 = Celular ("Apple", "Iphone 15 Pro", "96MP")

# Luego llamamos a pantalla el proceso de nuestra clase dandonos como resulado el metodo en accion
celular1.cortar()