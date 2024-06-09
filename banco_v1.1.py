import textwrap


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR${valor:.2f}\n'
        print('Operaçao realizada com sucesso.')
        print(f'Seu saldo atual é R${saldo:.2f}\n')
    else:
        print('Valor inválido')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo < valor > 500 and numero_saques >= limite_saques:
        print('Operaçao indisponivel no momento')
    else:
        saldo -= valor
        extrato += f'Saque:\tR${valor:.2f}\n'
        numero_saques += 1
        print('\nOperaçao realizada com sucesso.')
        print(f'Seu saldo atual é de R${saldo:.2f}')
        print(f'Voce ainda pode realizar {limite_saques - numero_saques} hoje.\n')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    if len(extrato) == 0:
        print('Sem movimentação bancária.')
    else:
        print('>>EXTRATO<<\n')
        print(extrato)
    return extrato


def criar_usuario(usuarios):
    cpf = input("Informe o cpf: ")
    cpf = cpf.replace('.', '')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado no sistema")
        return

    nome = input("Nome completo: ").rstrip()
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo (logradouro, nro, bairro, cidade-estado): ")
    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('\n Usuario cadastrado com sucesso')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada cm sucesso ! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario nao encontrado, retornando ao menu principal. ")



def menu():
    menu = """
    =====>>MENU<<=====
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [N] Nova Conta
    [L] Lista de contas
    [C] Novo Usuário
    [Q] Sair
    ==> """

    opcao = input(menu)
    opcao = opcao.lower().strip()
    return opcao


LIMITE_SAQUES = 3
AGENCIA = '001'

limite = 500
saldo = 2
extrato = ""
numero_saques = 2
lista_usuarios = []
lista_contas = []


while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input('Valor a ser depositado: R$'))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input('Digite o valor: R$'))

        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                              numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        criar_usuario(lista_usuarios)

    elif opcao == 'n':
        numero_conta = len(lista_contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, lista_usuarios)

        if conta:
            print(f"O numero da sua agencia é: {AGENCIA}, e o numero da sua conta corrente é {numero_conta}.\n")
            lista_contas.append(conta)


    elif opcao == 'l':
        for conta in lista_contas:
            linha = f'''\
                Agencia: \t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            '''
            print("=" *30)
            print(textwrap.dedent(linha))

    elif opcao == "q":
        print("Sessão encerrada\n")
        break

    else:
        print("Digite uma opção válida.")


