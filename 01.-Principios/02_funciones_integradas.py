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

<<<<<<< HEAD
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de Persona
juan = Persona("Juan", 30)

# Mostrar los nombres de atributos y métodos de la instancia juan
print(dir(juan))
=======
>>>>>>> 5aa36ef (function study)

