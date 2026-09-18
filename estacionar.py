import estado
def estacionarVaga():
    if(estado.vagas == 0):
        print("não há mais vagas")
    else:
        estado.vagas = estado.vagas - 1   