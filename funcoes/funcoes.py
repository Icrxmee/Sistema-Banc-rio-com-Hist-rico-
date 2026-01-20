from interfacee.interface import *
from time import sleep

def controlePrincipal():

    saldo = 0

    try:
 
        while True:

            a = menuPrincipal()

            match a:
                
                case "1":
                    saldo = deposito(saldo)
                
                case "2":
                    saldo = sacar(saldo)

                case "3":
                    verSaldo(saldo)

                case "4":
                    a = historico(a=True)

                case "0":
                    print("Saindo do Sistema")
                    sleep(1)
                    return

                case _:
                    print("Escolha uma opção válida")
    
    except KeyboardInterrupt:
        print("\nInterrompendo o sistema")
        linha()
        sleep(1)


def deposito(saldo):
    
    while True:

        try:
            linha()
            a = float(input("Quanto deseja depositar: "))
            saldo += a
            
            historico(a)
            return saldo

        except ValueError:
            print("Entrada inválida")

def sacar(saldo):

    while True:

        try: 
            linha()
            a = float(input("Quanto deseja sacar: "))
            saldo -= a
            return saldo
        
        except ValueError:
            print("Entrada inválida")

def verSaldo(saldo):

    linha()
    print(f"Você tem um saldo de: R$ {saldo:.2f}".replace(".",","))
    
def historico(a=False, b=False):

    lista = []
    
    if a is True:
        print(lista)

    
