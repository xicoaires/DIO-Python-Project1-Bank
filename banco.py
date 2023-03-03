bank_extract = []
balance = 0.0
WITHDRAW_LIMIT_VALUE = 500
WITHDRAW_LIMIT_DAILY = 3
withdraw_daily = 0

def deposit(balance):
    value = float(input("\nVocê escolheu a opção depósito.\nDigite o valor a ser depositado: R$ "))
    
    if value > 0:
        balance += value
        print(f"\nO valor de R$ {value:.2f} foi depositado com sucesso!\nSeu saldo atual é de R$ {balance:.2f}")
        bank_extract.append(f"Depósito: R$ {value:.2f}")
        input("\nAperte ENTER para voltar ao menu inicial")
    else:
        print("O valor informado é inválido!")
        input("\nAperte ENTER para voltar ao menu inicial")
    return balance

def withdraw(balance, withdraw_daily):

    if withdraw_daily < WITHDRAW_LIMIT_DAILY:
        value = float(input("\nVocê escolheu a opção sacar.\nDigite o valor a do saque: R$ "))
        if value > 0:
            if value <= balance:
                if value <= 500:
                    balance -= value
                    print(f"\nO valor de R$ {value:.2f} foi sacado com sucesso!\nSeu saldo atual é de R$ {balance:.2f}")
                    input("\nAperte ENTER para voltar ao menu inicial")
                    withdraw_daily += 1
                    bank_extract.append(f"Saque: R$ {value:.2f}")
                else:
                    print("Saque não realizado. O limite do saque é de R$ 500,00")
                    input("\nAperte ENTER para voltar ao menu inicial")
            else:
                print("Saque não realizado. Saldo insuficiente!")
                input("\nAperte ENTER para voltar ao menu inicial")
        else:
            print("Saque não realizado. O valor informado é inválido!")
            input("\nAperte ENTER para voltar ao menu inicial")
    else:
        print("Saque não disponível. Você ultrapassou o limite de 3 saques diários.")
        input("\nAperte ENTER para voltar ao menu inicial")
    
    return balance, withdraw_daily

def extract():
    for i in bank_extract:
        print(" " + i)
    input("\nAperte ENTER para voltar ao menu inicial")

menu = """
    ____________________________
    |    ..:: DIO BANK ::..    |
    |      ==== MENU ====      |
    |                          |
    | Digite a opção desejada: |
    |                          |
    |   1 - DEPOSITAR          |
    |   2 - SACAR              |
    |   3 - EXTRATO            |
    |   0 - SAIR               |
    |__________________________|

    Opção: """

while True:
    print(menu, end="")
    option = int(input())

    if option == 1:
        balance = deposit(balance)
        continue


    if option == 2:
        balance, withdraw_daily =  withdraw(balance, withdraw_daily)
        continue

    if option == 3:
        extract()
        continue

    if option == 0:
        print("O Dio Bank agradece. Até logo!")
        break

    else:
        print("Você digitou uma opção inválida. Tente Novamente!")
        input("\nAperte ENTER para voltar ao menu inicial")


