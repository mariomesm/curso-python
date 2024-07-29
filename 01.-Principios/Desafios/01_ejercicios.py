import math

#Mostrar el resultado con las siguientes operaciones en donde los operadores son 3 y 4 
def numerical_values():
    print(3+4)
    print(3-4)
    print(3*4)
    print(3%4)
    print(3/4)
    print(3**4)
    print(3//4)

numerical_values()

#Escribir cadenas y mostrar nombre,apellido,pais, un mensaje
def string_text():
    print('Mario')
    print('Martinez')
    print('México')
    print('Aprendiendo python')

string_text()

'''
Comprobar los tipos de datos de las siguientes datos 
10,9.8,3.14,4-4j,['Asabeneh','Python','Finlandia'],{nombre, apellido, pais}
'''
def type_data():
    print(type(10))
    print(type(9.8))
    print(type(3.14))
    print(type(4-4j))
    print(type(['Asabeneh','Python','Finlandia']))
    print(type({'nombre':'Mario','apellido':'Martinez','pais':'México'}))

type_data()

#Calcular la distancia euclidiana donde (3,1) (8,10)

def distance_euclidean(q1,q2,p1,p2):
    result = math.sqrt((q1-q2)**2+(p1-p2)**2)
    return result

distancia = distance_euclidean(3,8,1,10)
print(f"La distancia recorrida es:{distancia}")