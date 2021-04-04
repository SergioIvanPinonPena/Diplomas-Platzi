termina = True
potencia = 0
while termina:
    resultado = 2**potencia
    if resultado >= 1000:
        termina = False
    else:
        print(f'2^{potencia} = {resultado}')
        potencia = potencia + 1
        termina = True