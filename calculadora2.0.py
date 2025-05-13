# Função para exibir o menu da calculadora
def exibir_menu():
    print("\n--- Calculadora com Histórico ---")
    print("Escolha uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Exibir histórico")
    print("6. Sair")

# Função para realizar a operação
def realizar_operacao(opcao, num1, num2):
    if opcao == 1:
        return num1 + num2, f"{num1} + {num2} = {num1 + num2}"
    elif opcao == 2:
        return num1 - num2, f"{num1} - {num2} = {num1 - num2}"
    elif opcao == 3:
        return num1 * num2, f"{num1} * {num2} = {num1 * num2}"
    elif opcao == 4:
        if num2 == 0:
            return None, "Erro: Divisão por zero!"
        return num1 / num2, f"{num1} / {num2} = {num1 / num2}"

# Lista para armazenar o histórico das operações
historico = []

# Função principal da calculadora
def calculadora():
    while True:
        exibir_menu()
        opcao = int(input("\nDigite a sua escolha (1-6): "))

        if opcao == 6:  # Sair
            print("Saindo da calculadora.")
            break

        elif opcao == 5:  # Exibir histórico
            print("\n--- Histórico de Operações ---")
            if len(historico) == 0:
                print("Nenhuma operação realizada.")
            else:
                for item in historico:
                    print(item)
            continue

        elif opcao in [1, 2, 3, 4]:  # Operações básicas
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            resultado, descricao = realizar_operacao(opcao, num1, num2)

            if resultado is None:
                print(descricao)
            else:
                print(f"Resultado: {resultado}")
                historico.append(descricao)  # Armazena a descrição no histórico

        else:
            print("Opção inválida. Tente novamente.")

# Executar a calculadora
calculadora()
