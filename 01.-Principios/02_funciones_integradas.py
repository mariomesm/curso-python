#abs()
print(abs(-10))
print(abs(-1.4))

#all()
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(all([True, 1, True]))  # Debería imprimir: True
print(all([True, 0, True]))  # Debería imprimir: False

#any

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(any([None,False,0])) #Debería de imprimir False
print(any([True,1,True]))#Deberia de imprimir True

#bin()

print(bin(10))
print(bin(100))
print(format(10,'b')) #con format puedo quitar el valor de 0b colocando el valor de 'b'

#bool

print(bool([])) #Debera de mostrar un valor falso
print(bool(1)) #deberia de mostrar true

#breakpoint()
'''
def calcular_suma(a, b):
    breakpoint()  # Aquí se detendrá la ejecución
    suma = a + b
    return suma

resultado = calcular_suma(5, 3)
print(resultado)
'''
#bytearray 

cadena = 'Hola mundo'
datos = bytearray(cadena,'utf8')
print(datos)

data = bytearray([65,66,67,68])
print(data)
data[2] = 80
print(data)

#bytes  no se puede modificar su resultado como bytearray

data = bytes([65,66,67])
print(data) #Muestra 'ABC' 

#callable

def my_function():
    print('Hola mundo')

def call_a_function(obj):
    if callable(obj):
        obj()
    else:
        print('No es un callable')

call_a_function(my_function) #Muestra lo que imprime mi funcion my_function
call_a_function(10) #Muestra el mensaje no es un callable
        
#chr convierte un  codigo unicode en su caracter correspondiente 

print(chr(100))
print(chr(8364))

#complex un número complejo consta de una parte imaginaria y una real donde los numeros son numeros reales y j la parte imaginaria

print(complex(3,4)) #muestra 3+4j
print(1+2j)

#delattr
class Persona: 
    def __init__(self,nombre):
        self.nombre = nombre

persona = Persona("Pedro")
persona.age = 30
persona.nat = 'Mexico'
print(persona.__dict__) #Me muestra el diccionario de persona
delattr(persona,'nat') #Elimina de mi diccionario la propiedad nat
print(persona.__dict__)

#divmod toma dos numeros (dividendo,divisor) devuelve una tupla

print(divmod(10,3))
print(divmod(-10,3)) #con valores negativos la regla de redondeo es hacia abajo valor(-4,2)
'''
El cociente de -10 // 3 es -4 porque -10/3 da -3.333 y al redondear hacia abajo se obtiene -4
El resto es 2 porque -4 * 3 +2 = -10 que es el valor que estamos pasando como dividiendo
'''
print(divmod(10.5,3.2)) #(3.0,0.89) 3*3.2+.89 = 10.5

"""
enumerate devuelve un objeto enumerado que es un iterador que nos permite recorrer una secuencia de valores
pero no podemos acceder directamente como una lista, por lo cual utilizamos list()
"""
lista = ['spring','summer','fall','winter']
print(list(enumerate(lista)))

for index,li in enumerate(lista):
    print(f"indice:{index} valor:{li}")

#eval() evalua una cadena y regresa un resultado

cadena_numeros = '10 + 15 * 3'
nuevo_array ='[10,45,12,5]'
print(f"el resultado es: {eval(cadena_numeros)}")
print(f"el resultado es: {eval(nuevo_array)}")

#filter()

valores = ['sol','luna','estrella','cielo','mar']
def list_cadena(list):
    return len(list) > 3
caracter_tres = filter(list_cadena,valores)
print(list(caracter_tres))

dict_ejemplo = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
claves_valores = filter(lambda item:item[1]>2, dict_ejemplo.items())
dict_filtrado = {k:v for k, v in claves_valores}
print(dict_filtrado)
