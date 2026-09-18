vagas = 150

#consultar vagas para ver quantas estao disponiveis
def consultarVagas():
    print(vagas)

#ocupar as vagas e atualizar o valor 
def estacionar():
    global vagas
    if(vagas == 0):
        print("não há mais vagas")
    else:
        vagas = vagas - 1

#liberar um vaga no estacionamento
def liberarVaga():
    global vagas
    
    vagas = vagas + 1
    


if __name__=="__main__":
    consultarVagas()
    estacionar()
    consultarVagas()
    liberarVaga()
    consultarVagas()