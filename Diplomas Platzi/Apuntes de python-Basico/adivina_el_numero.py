import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Es un numero mas grande')
            numero_elegido = int(input('Elige otro numero: '))
        else:
            print('Es un numero Mas Pequeño')
            numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste')

if __name__ == '__main__':
    run()