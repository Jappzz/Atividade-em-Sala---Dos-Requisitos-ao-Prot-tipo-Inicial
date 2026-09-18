vagas = 150
def consultarVagas():
    print(vagas)

def estacionar():
    global vagas
    vagas = vagas - 1

def liberarVaga():
    global vagas
    vagas = vagas + 1
    


if __name__=="__main__":
    consultarVagas()
    estacionar()
    consultarVagas()
    liberarVaga()
    consultarVagas()