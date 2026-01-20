from interfacee.interface import *
from time import sleep

def controlePrincipal():

    saldo = 0 # Saldo do Controle
    movimentação = [] # 
    
    try:
 
        while True:

            a = menuPrincipal()

            match a:
                
                case "1":
                    saldo = deposito(saldo, movimentação)
                
                case "2":
                    saldo = sacar(saldo, movimentação)

                case "3":
                    verSaldo(saldo)

                case "4":
                    historico(movimentação, mostrar= True)

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


def deposito(saldo, movimentação):
    
    while True:

        try:
            linha()
            a = float(input("Quanto deseja depositar: "))
            
            if a <= 0:
                print("Valor inválido")
                return saldo

            saldo += a            
            movimentação.append(("+", a))
            return saldo

        except ValueError:
            print("Entrada inválida")

def sacar(saldo, movimentação):

    while True:

        try: 
            linha()
            a = float(input("Quanto deseja sacar: "))
            
            if a > saldo or a <= 0:
                print("Valor inválido")
                return saldo
            
            saldo -= a
            movimentação.append(("-", a))
            return saldo
        
        except ValueError:
            print("Entrada inválida")

def verSaldo(saldo):

    linha()
    print(f"Você tem um saldo de: R$ {saldo:.2f}".replace(".",","))
    
def historico(movimentação, mostrar= False):

    if mostrar:
        linha()

        if not movimentação:
            print("Nenhuma movimentação recente")

        else:
            for tip, val in movimentação:
                print(f"{tip} R$ {val:.2f}".replace(".",","))
