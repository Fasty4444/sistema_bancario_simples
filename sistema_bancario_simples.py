saldo_conta = 0
limite_por_saque = 500
limite_saque_dia = 3
contador_saque = 0
extrato = []

while True: 
    menu = print("""
----------------- MENU -----------------

 {1} Depositar
 {2} Sacar
 {3} Extrato
 {4} Sair
--------------------------------------------""")
    opcao = int(input("Digite uma opção: "))
    
    # Depósito
    if opcao == 1:
        deposito = float(input("Valor do depósito: "))

        if deposito <= 0:
            print("Valor inválido, informe um valor positivo!")

        else:
            print(f"Depósito de R${deposito:.2f}, realizado com sucesso!")
            saldo_conta += deposito
            extrato.append(f"Depósito: +R${deposito:.2f}")

# Saque
    elif opcao == 2:
        if contador_saque >= limite_saque_dia:
            print("Limite de saques diário atingido!")
            continue

        saque = float(input("Valor do saque: "))

        if saque > saldo_conta:
            print("Saldo insuficiente!")

        elif saque > limite_por_saque:
            print("Limite de saque atingido!")

        elif saque <= saldo_conta:
            print(f"Saque de R${saque:.2f}, realizado com sucesso!")
            saldo_conta -= saque
            contador_saque += 1
            extrato.append(f"Saque: -R${saque:.2f}")
# Extrato

    elif opcao == 3:
        print("\n----- EXTRATO -----")
        if extrato:
            for transacao in extrato:
                print(transacao)
        else:
            print("Nenhuma movimentação registrada.")
        print("-------------------")

    # Sair
    elif opcao == 4:
        print("🏦 Obrigado por usar nosso banco! Até mais! 👋")
        break  # Encerra o programa

    else:
        print("❌ Opção inválida! Escolha uma opção entre 1 e 4.")