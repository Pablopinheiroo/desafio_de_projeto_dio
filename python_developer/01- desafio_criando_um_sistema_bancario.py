menu = """
----- INTERFACE DO BANCO -----
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0


def titulo_menu(txt):
    titulo = f" {txt}: "
    titulo = titulo.center(50, '*')
    return titulo


while True:

    opcao = input(menu).lower().strip()[0]
    print("")

    if opcao == "d":
        novo_titulo = titulo_menu("Depósito")
        print(novo_titulo)

        deposito = float(input("Informe quanto deseja depositar? "))
        if deposito > 0:
            print('Deposito bem sucedido!')
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            saldo += deposito
            print("*" * (len(novo_titulo)))

        else:
            print("Operação falhou! O valor informado é inválido")
            print("*" * (len(novo_titulo)))

    elif opcao == "s":
        novo_titulo = titulo_menu("Saque")
        print(novo_titulo)
        saque = float(input("Informe o valor do saque: "))
        if saldo == 0:
            print("Operação falhou! Nenhum valor em caixa foi encontrado! ")

        if LIMITE_SAQUES == 0:
            print("Operação falhou! Número máximo de limite de Saque excedido.")

        if saque > 500:
            print("Operação falhou! Número máximo de saques excedido.")

        if (saldo > 0) and (LIMITE_SAQUES > 0) and (saque <= 500):
            extrato += f"Saque: R$ {saque:.2f}\n"
            saldo -= saque
            LIMITE_SAQUES -= 1
        print("*" * (len(novo_titulo)))

    elif opcao == "e":
        novo_titulo = titulo_menu("Extrato")
        print(novo_titulo)
        if len(extrato) > 0:
            print(f"{extrato}\n\nSaldo: R$ {saldo:.2f}")
        else:
            print('Nenhum Extrato para informar!')

        print("*"*len(novo_titulo))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
