from time import sleep

menu = """
    >>MENU<<
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
    
    ==> """

saldo = 0
limite_saque = 500
extrato = []
numero_saques = 3
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    opcao = opcao.lower().strip()

    if opcao == "d":
        print(">>Deposito<<\n")
        valor = int(input("Valor a ser depositado: R$"))
        if valor <= 0:
            print("Valor invalido")
        else:
            saldo += valor
            extrato.append(valor)

    elif opcao == "s":
        print(">>Sacar<<\n")
        if numero_saques <= 0:
            print("Número de saques diários excedido.")
        else:
            while True:
                valor_saque = int(input("Valor a ser sacado R$"))
                if 0 < valor_saque > 500:
                    print("Valor acima do limite. \n")
                elif valor_saque > saldo:
                    print("Saldo indisponível.")
                else:
                    saldo -= valor_saque
                    numero_saques -= 1
                    extrato.append(-valor_saque)

                    sleep(2)
                    print("Retire seu dinheiro")
                    sleep(2)
                    print("Retire seu comprovante.")
                    break

    elif opcao == "e":
        print(">>Extrato<<\n")
        for valor in extrato:
            if valor > 0:
                print(f"Deposito de R${valor:.2f}.")
            else:
                print(f"Saque de R${valor:.2f}.")
        print(f'\nSeu valor disponível para saque é R${saldo:.2f}')
        print(f"Você ainda tem {numero_saques} saques.")

    elif opcao == "q":
        print("Sessão encerrada\n")
        break

    else:
        print("Digite uma opção válida.")
