menu = """
Escolha a opção desejada:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor_depositado = float(input("Qual valor deseja depositar?"))
        
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: {valor_depositado:.2f}\n "
        else: 
            print("Operação falhou. O valor informado é errado!")
            
    elif opcao == "s":
        valor_saque = float(input("Informa o valor do saque: "))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques =  numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou você não tem saldo sufuciente!")
        elif excedeu_limite:
            print("Operação falhou, o valor do saque excede o limite!")
        elif excedeu_saques:
            print("Operação falhou, número máximo de saques excedido!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: {valor_saque:.2f}\n"
        else:
            print("Operação falhou. O valor informado é inválido")
    elif opcao == "e":
        print("\n=====================EXTRATO=================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:{saldo:.2f}")
        print("================================================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")