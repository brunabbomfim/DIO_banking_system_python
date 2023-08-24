menu = """

Qual operação deseja realizar?

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair

=> """

operacao = """

Deseja realizar outra operação?

[s] Sim
[n] Nao

=> """

confirmacao = """

[s] Sim
[n] Nao

=> """

saldo = 0
limite = 500
lista_valores = []
extrato = ""
numero_saques = 0
limite_saque = 3

while True:

    opcao = input(menu)

    if opcao == "1":  
        print("Deposito")
        deposito = int(input("Qual valor deseja depositar: "))

        if deposito <= 0:
            print("Valor inválido!")
           
        elif deposito > 0:
            print(f"O valor de {deposito} será depositado. Confima? ")
            confirmacao1 = input(confirmacao)

            if confirmacao1 == "s":
                lista_valores.append(f"Deposito: {deposito}")
                saldo += deposito
                print("Depósito realizado com sucesso!")
         
            elif confirmacao1 == "n":
                print("Operação cancelada!")

            else: 
                print("Operação inválida!")       
    
    elif opcao == "2":
        saque = int(input("Digite o valor do saque: "))
        if saque <= 0:
            print("Valor inválido!")

        elif saque > 0:

            if saldo < saque:
                print("Valor indisponível para saque!")
            elif saldo >= saque:
                print(f"Valor do saque: {saque}")
                confirmacao1 = input(confirmacao)
                if confirmacao1 == "s":
                    lista_valores.append(f"Saque: -{saque}")
                    saldo -= saque
                    print("Saque realizado com sucesso!")
         
            elif confirmacao1 == "n":
                print("Operação cancelada!")

            else: 
                print("Operação inválida!")
        
    
    elif opcao == "3":
        print(f' Saldo: R$ {saldo}')
        print(f"Valores depositados: {lista_valores}")
    
    elif opcao == "0":
        break

    else: 
        print("Operação inválida, por favor digite novamente a opção desejada")
    
