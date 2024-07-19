#Variables se utiliza la convención snake_case

my_string_variables = 'My string variable'
print(my_string_variables)

my_int_variable = 5
print(my_int_variable)

#Se puede declarar varias variables en una misma linea 

first_name, last_name, country = 'Mario','Martinez','México'

print('First name', first_name)
print('Last name', last_name)
print('county',country)
#podemos declarar varibles utilizando palabras reservadas empezando con un _ al inicio

_if = 'Estoy ocupando una palabra reservada'

#Podemos obtener información del usuario mediante la función input()

age = input('Cúal es tu edad:')
print(age)

#conversion de un tipo de dato 

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

_str = 'Hola mundo' #di queremos utilizar palabras reservadas como variables
print('cadena',_str)
list_caracteres = list(_str)
print('lista',list_caracteres)

