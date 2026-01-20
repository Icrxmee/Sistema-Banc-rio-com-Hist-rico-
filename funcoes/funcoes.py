from interfacee.interface import *
from time import sleep

lista = []

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
                    historico(mostrar= True)

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
            
            historico(tipo= "+", valor= a)
            return saldo

        except ValueError:
            print("Entrada inválida")

def sacar(saldo):

    while True:

        try: 
            linha()
            a = float(input("Quanto deseja sacar: "))
            saldo -= a

            historico(tipo= "-", valor= a)
            return saldo
        
        except ValueError:
            print("Entrada inválida")

def verSaldo(saldo):

    linha()
    print(f"Você tem um saldo de: R$ {saldo:.2f}".replace(".",","))
    
def historico(tipo= None, valor= None, mostrar= False):

    global lista
    
    if tipo is not None and valor is not None:

        lista.append((tipo, valor)) 

    if mostrar:
        linha()

        if not lista:
            print("Nenhuma movimentação recente")

        else:
            for tip, val in lista:
                print(f"{tip} R$ {val:.2f}".replace(".",","))
