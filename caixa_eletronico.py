saldo = 7000
opçao = ""

while opçao != "3":
    print("\n=== Caixa Eletrônico ===")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Sair")
    print("-----------------")

    opçao = input("Escolha uma opção: ")

    if opçao == "1":
        print(f"Seu saldo é: R$ {saldo}")

    elif opçao == "2":
       valor = float(input("Digite o valor para sacar: "))
       if valor <= saldo:
           saldo -= valor
           print(f"Saque de R$ {valor} realizado com sucesso.")
           print(f"Saldo atual: R$ {saldo}")
       else:
           print("Saldo insuficiente!")

    elif opçao == "3":
         print("Encerrando... Até mais!")

    else:
        print("Opção inválida.")