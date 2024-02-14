# Principio de sustitucion de liskov, nos dice que debemos poder craer una clase A y que esa clase A le herede a la clase B, siendo asi que todo lo que hace A
# Lo haga B es decir si B es una subclase de A debe poder realizar todo lo que A pueda hacer

# aca tenemos el primer codigo, el cual esta erroneo, ¿por que?
# class Ave(): # clase padre la cual puede volar
#     def volar(self):
#         return  "Estoy volando" 
    
# class Pinguino(Ave): # clase B que hereda de A
#     def volar(self):
#         return "No puedo volar"
        
# def hacer_volar(ave = Ave): # Funcion para retornar lo que haga nuestra clase
#     return ave.volar()

# print(hacer_volar(Pinguino())) # al momento de pedir que nuestra clase B realice la accion de la clase A no es capaz de hacerla tenemos un problema debemos solucionar

# practicamente porque al momento de que pinguino requiera hacer su metodo no puede realizar todo lo que la clase A pueda hacer entonces debemos reescribir este codigo
# siguiento el metodo de sustitucion de Liskov

# nuevo codigo siguiendo el principio de sustitucion de Liskov
class Ave(): # hacemos que la clase A pueda admitir todo lo que sus subclases puedan hacer
    pass

class AveVoladora(Ave): # clase B que hereda de A
    def volar(self): 
        return "Estoy volando" # esta clase puede volar
    
class AveNoVoladora(Ave): # clase C que hereda de A, como clase B puede volar y la clase C no es categorizada para cumplir lo mismo no se ejecuta
    pass    

# pero si podemos seguir creando mas subclases de aves como aves nadadoras y que cumplan su funcion como una ave que puede nadar