import math
'''
Escribe un comentario en Python
Declarar una variable de nombre y asignarle un valor
Declarar una variable de apellido y asignarle un valor
Declarar una variable con nombre completo y asignarle un valor
Declarar una variable de país y asignarle un valor
Declarar una variable de ciudad y asignarle un valor
Declarar una variable de edad y asignarle un valor
Declarar una variable de año y asignarle un valor

'''
comment = 'python'
first_name = 'Mario '
last_name = 'Martinez'
name = first_name + last_name
country = 'México'
age = 24
anio = 2024
is_married = False

#1.-Comprueba el tipo de datos de todas tus variables usando la función incorporada type()
print(type(comment)) #str
print(type(first_name)) #str
print(type(last_name)) #str
print(type(name)) #str
print(type(country)) #str
print(type(age)) #int
print(type(anio)) #int
print(type(is_married)) #booolean

#2.-Usando la función incorporada len() , encuentre la longitud de su nombre

print(f"La longitud de el nombre es: {len(name)}")

#3.-Compara la longitud de tu nombre y tu apellido

print(f"La longitud de mi nombre es: {len(first_name)}")
print(f"La longitud de mi apellido es: {len(last_name)}")

'''
4.-Declara 5 como num_one y 4 como num_two
    i.-Sume num_one y num_two y asigne el valor a una variable total
    ii.-Resta num_two de num_one y asigna el valor a una variable diff
    iii.-Multiplica num_two y num_one y asigna el valor a una variable producto
    iv.-Dividir num_one por num_two y asignar el valor a una variable división
    v.-Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
    vi.-Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
    vii.-Encuentra la división del piso de num_one por num_two y asigna el valor a una variable floor_division
'''
num_one = 5
num_two = 4

total = num_one + num_two
diff= num_two - num_one
producto = num_two * num_one
division = num_one /num_two
resto = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(f"El total es: {total}")
print(f"El valor de la resta es: {diff}")
print(f"El resultado de la multiplicación es: {producto}")
print(f"El resultado de la división es: {division}")
print(f"El resultado de el resto es: {resto}")
print(f"El resultado de elevar a la potencia es: {exp}")
print(f"El valor de la disión de piso es: {floor_division}")

'''
5.-El radio de un círculo es de 30 metros.
    i.-Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle
    ii.-Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle
    iii.-Tome el radio como entrada del usuario y calcule el área.
'''
radio = 30

area_of_circle = math.pi * (radio)**2
circum_of_circle = ((2 * math.pi) * (radio))
print(f"El area del circulo es: {area_of_circle}")
print(f"La circunferencia del circulo es: {circum_of_circle}")

new_radio = float(input("Digite el radio del circulo:"))
new_area_of_circle = (math.pi * pow(new_radio,2))
print(f"El area del circulo con radio {new_radio} es: {new_area_of_circle}")

#6.-Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario
# y almacenar el valor en sus nombres de variable correspondientes.

input_name = str(input("Digita tu nombre: "))
input_last_name =str(input("Digita tu apellido: "))
input_country = str(input("Digita tu pais: "))
input_age = int(input("Digita tu edad: "))

data_user = {
    'user_name':input_name,
    'user_last_name':input_last_name,
    'user_country': input_country,
    'user_age':input_age
}
print(data_user)