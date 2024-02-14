# en este ejercicio desarrollaremos un analizador de sentimientos, usando el chatbot de intelegencia artificial
# para esto usaremos el chatbot general de openai empresa muy reconocida

import openai # instalamos e importamos su libreria para su uso 

openai.api_key_path = "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" # luego creamos una api desde la cuenta oficial de openai para crear nuestro "bot" calculador de sentimientos
system_rol = '''Hace cuenta que sos un analizador de sentimientos.
                 Yo te paso los sentimientos y tu analizas los sentimientos de los mensajes
                 me daras una respuesta con al menos un caracter y como maximo 4 caracteres
                 SOLO RESPUES NUMERICAS, donde -1 es negatividad maxima, 0 es neutro y  1 es positivo maxima
                 (puedes responder con ints o floats)'''  #aca le damos el rol a nuestro bot es decir como se tiene que comportar y todo lo que debe realizar para analizar dichos sentimientos

mensajes = [{"role": "system", "content": system_rol}] # luego establecemos los parametros de como debe tomar su rol y como definir al usuario el cual le pasara dicho nivel de sentimientos

# creamos una clase la cual se encargue de formatear el texto de entrada y salida cada vez que se hicieran un afirmacion con el chat asi no tendriamos que al momento de querer
# agregar una nueva linea de calificacion de sentimientos deberiamos cambiar toda la condicional if anidada
class Sentimiento():
    def __init__(self,nombre,color) -> None:
        self.nombre = nombre
        self.color=color

# usamos str para devolver todo esto como un formato de texto sabiendo que el metodo transformaria todo a un string
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37]".format(self.color,self.nombre)
            

class analizadordesentimientos(): # luego generamos nuestra clase analizadora de sentimientos

# como usaremos esto para recorrer los sentimientos debe tener sus atributos a evaluar
    def __init__(self,rangos) -> None:
        self.rangos = rangos
        
    def analizar_sentimiento(self,polaridad): # El metodo que neceistaremos que realice, el cual es una polaridad desde el -1 hasta el 1
        for rango, sentimiento in self.rangos: # todo con un for y nuestro metodo de analizar sentimiento
            if rango[0] < polaridad <= rango[1]: # recorremos todo con la condicion de nuestro if
                return sentimiento
        return Sentimiento("Muy negativo","31")# devolvemos todos los valores al momento que se recorra y no tenga nada esperado de nuestro for
    
# en el primer ejemplo al fianalizar todo el ejercicio era un codigo bastante tosco y muy dependiente de un solo metodo
# cosa que nos afecta sabiendo los pirncipios solid asi que los cambios fueron para hacer un codigo mas completo y escalable

rangos = [
    {(-0.6,-0.3),Sentimiento("negativo","31")},
    {(-0.3,-0.1),Sentimiento("algo negativo","31")},
    {(-0.1,0.1),Sentimiento("Neutral","33")},           # creamos toda la lista de rangos la cual va a ser el argumento de nuestro parametro en la clase para poder instarciarla
    {(0.1,0.4),Sentimiento("algo positivo","32")},
    {(0.4,0.9),Sentimiento("positivo","32")},
    {(0.9,1),Sentimiento("muy posiivo","32")},
]

analizador = analizadordesentimientos(rangos) # instanciamos la clase

# con este ciclo while true, hacemos un ciclo infinito el cual analizara todas las frases o afirmaciones que le pasemos junto a la extension de openai y la api creada
while True:
    user_prompt =  input("\x1b[1;33m" + "\n Dime algo: " + "\x1b[0;37m")
    mensajes.append({"role":"user","content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        menssages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choises[0].menssage["content"]
    mensajes.append({"role":"assistant","content":respuesta})
    
    senimiento = analizador.analizar_sentimiento(respuesta)
    print(senimiento)
# y realizamos las pruebas 