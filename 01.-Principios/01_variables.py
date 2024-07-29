#Variables se utiliza la convención snake_case

my_string_variables = 'My string variable'
print(my_string_variables)

my_int_variable = 5
print(my_int_variable)

#Se puede declarar varias variables en una misma línea

first_name, last_name, country = 'Mario','Martinez','México'

print('First name', first_name)
print('Last name', last_name)
print('county',country)
#Podemos declarar variables utilizando palabras reservadas empezando con un _ al inicio

_if = 'Estoy ocupando una palabra reservada'

#Podemos obtener información del usuario mediante la función input()

age = input('Cúal es tu edad:')
print(age)

#conversión de un tipo de dato 

#int to float
num_int = 100
print('numero_entero',num_int)
num_float = float(num_int)
print('numero_flotante', num_float)

#int to str

num_int_dos = 10
print('numero entero',num_int_dos)
num_str = str(num_int_dos)
print('cadena texto',num_str)

#str to list

_str = 'Hola mundo' #Si queremos utilizar palabras reservadas como variables
print('cadena',_str)
list_caracteres = list(_str)
print('lista',list_caracteres)

#list to tupla

lst = [1,2,3]
tup = tuple(lst)
print(tup)

lst_to_set = [1,2,3,4,5]
unique_set = set(lst_to_set)
print(unique_set)


#concatenación de variable

prueba = 'Curso python'
print('Este es un mensaje del',prueba)

#Python es de tipado dinámico, podemos especificar que tipo de valor espera pero 
#no toma estrictamente ese valor podemos pasarle un entero en la parte de un str y lo acepta
def saludo (address:str,phone:int):
    return     f"su dirección es: {address}, y su telefono es: {phone}"

mensaje = saludo("dirección",12345)
print(mensaje)
