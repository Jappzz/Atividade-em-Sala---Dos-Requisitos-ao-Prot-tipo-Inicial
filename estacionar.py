from main import vagas
def estacionarVaga():
    global vagas
    if(vagas == 0):
        print("não há mais vagas")
    else:
        vagas = vagas - 1   