def imprimir_mensaje ():
    print("Mensaje Especial")
    print("Estoy aprendiendo usar funciones")



"""print("Mensaje Especial")
print("Estoy aprendiendo usar funciones")
print("Mensaje Especial")
print("Estoy aprendiendo usar funciones")
print("Mensaje Especial")
print("Estoy aprendiendo usar funciones")"""

def saludo (str):
    '''Recibe un string y regresa un saludo 
    concatenando ese string en el saludo '''
    print("Hola")
    print("Como estas")
    print("Elegiste la opcion " + str)
    print("Adios")

'''opcion = int(input("Elige una opcion (1, 2, 3):  "))

if opcion == 1:
    saludo("1")
elif opcion == 2:
    saludo("2")
elif opcion == 3:
    saludo("3")
else: 
    print("Eligue una opcion valida")'''

def suma (a , b):
    '''Recibe 2 numeros, las suma y retorna los numeros sumados '''
    print('Se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma(1,4)
print(sumatoria)