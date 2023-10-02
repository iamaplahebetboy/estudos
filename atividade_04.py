
saldo_conta = 1000.00


def consultar_saldo():
    print(f"Seu saldo atual é: R$ {saldo_conta:.2f}")


def sacar_dinheiro(valor):
    global saldo_conta
    if valor <= saldo_conta:
        saldo_conta -= valor
        print(f"Você sacou: R$ {valor:.2f}")
        print(f"Seu saldo atual é: R$ {saldo_conta:.2f}")
    else:
        print("Saldo insuficiente. Não é possível sacar o valor desejado.")


def depositar_dinheiro(valor):
    global saldo_conta
    saldo_conta += valor
    print(f"Você depositou: R$ {valor:.2f}")
    print(f"Seu saldo atual é: R$ {saldo_conta:.2f}")


while True:
    print("\nCaixa Eletrônico Simulado")
    print("1. Consultar Saldo")
    print("2. Sacar Dinheiro")
    print("3. Depositar Dinheiro")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        consultar_saldo()
    elif escolha == '2':
        valor = float(input("Digite o valor que deseja sacar: "))
        sacar_dinheiro(valor)
    elif escolha == '3':
        valor = float(input("Digite o valor que deseja depositar: "))
        depositar_dinheiro(valor)
    elif escolha == '4':
        print("Obrigado por usar o Caixa Eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
