# aca creamos una clase, esa clase le definimos sus atributos los cuales resaltan en Marca, Modelo, Camara, para "instanciar" una clase lo cual se refiere a crear un objeto
# creamos nuestra variable celular y como valor le pasamos la clase
class Celular():
    Marca = "Samsumg"
    Modelo = "S23"
    Camara = "48MP"

celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

# Para observar que contiene cada celular(Objeto), debemos llamar al celular que deseemos y pedirle que atributo queremos que muestre
print(celular1.Camara)

# Se ha de resaltar que estos son atributos estaticos, es decir si queremos que un celular contenga otros atributos debemos cambiar los ya existentes en la clase
# O en su defecto debemos cambiarlos fuera de la clase reemplazando los valores, algo que es tardado y considerado mala practica 