class Cuenta():
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = int(cantidad)
    
    def mostrar(self):
        print(f"El titular de la cuenta es: {self.titular}")
        print(f"La cuenta posee un valor de: {self.cantidad}")

    def ingresar(self):
        if self.cantidad == str():
            print("Deposito exitoso")
        else:
            print("Nada")

    def retirar(self):
        canti = self.cantidad - self.cantidad
        canti = self.cantidad
        if canti < self.cantidad:
            print("retiro exitoso")
        else:
            print("retiro no exitoso")
          
titular = "Daniel"
cantidad = int(input("Ingrese el monto a depositar: $"))

cuenta = Cuenta(titular, cantidad)

cuenta.ingresar()