def conversor(tipo_pesos , valor_dolar):
    '''Recibe un string y un int y regresa un print ya con el resultado '''
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰

1-Pesos colombianos
2-Pesos argentinos
3-Pesos mexicanos

Eligue una opcion: """

opcion = input(menu)

if opcion == "1":
    conversor("colombianos" , 3661.7)
elif opcion == "2":
    conversor("argentinos" , 91.81)
elif opcion == "3":
    conversor("mexicanos" , 20.31)
else:
    print("Ingresa una opcion correcta")
