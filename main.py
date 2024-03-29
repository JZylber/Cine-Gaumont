boleteria_abierta = True
while(boleteria_abierta):
    opcion = int(input(
    '''
    Elija una función:
    1) Relatos Salvajes (600p)
    2) Esperando la Carroza (400p)
    3) El secreto de sus ojos (500p)
    4) Cerrar boletería
    '''))
    if opcion == 4:
        boleteria_abierta = False
