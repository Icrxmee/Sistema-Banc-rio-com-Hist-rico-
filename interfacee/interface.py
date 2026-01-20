from time import sleep

def linha():
    print("~" * 40)

def menuInicio():

    linha()
    print("Bem-Vindo ao Nosso Sistema Bancário".center(40))
    linha()
    sleep(1)

def menuPrincipal():

    menuInicio()

    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Saldo")
    print("4 - Ver Histórico")
    print("0 - Sair")
    a = input("Acessar: ")
    return a
    
