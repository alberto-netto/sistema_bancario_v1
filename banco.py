menu = """
=========Escolha a função que deseja executar=========

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

======================================================
"""
saldo = 0
limite_saque = 500
limite_deposito = 5000
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_do_deposito = float(input("Por favor, informe o valor a ser depositado: \n R$ "))
        if valor_do_deposito > limite_deposito:
            print(f"Não é possível realizar a operação, o limite de depósito no caixa eletrônico é de R$ {limite_deposito}")
            print("======================================================")

        elif valor_do_deposito > 0:

            saldo += valor_do_deposito
            extrato += f"Depósito de R$ {valor_do_deposito:.2f} Efetuado com sucesso\n"

            print(f"Seu novo saldo é de R$ {saldo}\n")
            print("======================================================")
        else:
            print("Operação inválida, por favor informe um valor válido")
            print("======================================================")
    elif opcao == 2:
        valor_do_saque = float(input("Digite o valor a ser sacado: \n"))

        excedeu_saldo = valor_do_saque > saldo
        excedeu_limite = valor_do_saque > limite_saque
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Não é possível realizar a operação, seu saldo R$ {saldo} é insuficiente para realizar a operação")
            print("======================================================")
        
        elif excedeu_limite:
            print(f"Não é possível realizar a operação, o limite de saque no caixa eletrônico é de R$ {limite_saque}")
            print("======================================================")
        
        elif excedeu_saques:
            print(f"Não é possível realizar operação, o limite de saques é de {LIMITE_SAQUES} saques")
            print("======================================================")
        
        elif valor_do_saque > 0:
            saldo -= valor_do_saque
            numero_de_saques += 1
            extrato += f"Saque de R$ {valor_do_saque:.2f} Efetuado com sucesso\n"
            
            print(f"Saque de R$ {valor_do_saque} realizado com sucesso!, \n novo saldo de R$: {saldo}")
            print("======================================================")

        else:
            print("Não é possível realizar operação, valor do saque é inválido")
            print("======================================================")
        
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0:
        break
    else:
        print("Opção inválida, por favor, selecione uma das opções disponíveis no menu.")