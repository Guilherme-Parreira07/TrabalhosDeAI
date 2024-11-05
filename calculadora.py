
#Função para soma
def soma(x, y):
    return x + y

#Função para multiplicação
def multiplicação(x, y):
    return x * y

# Função para subtração
def subtração(x, y):
    return x - y

#Função para divisão
def divisão (x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

# Função do histórico para adicionar e manter a lista com as 5 últimas operações
def add_histórico(operação, num1, num2, result):
    histórico.append(f"{operação}: {num1} e {num2} = {result}")
    if len(histórico) > 5:
        histórico.pop(0)
        
#Função principal
def calculadora():
    while True:
       operação = input ("Escolha a operação: ")
        if operação in ["subtração", "soma", "multiplicação", "divisão"]:
            num1 = float(input("Digite o primeiro número:"))
            num2 = float(input("Digite o segundo número:"))
            if operação == "subtração":
                result = subtração(num1, num2)
                print("Resultado da subtração: " + str(result))
            elif operação == "soma":
                result = soma(num1, num2)
                print("Resultado da soma: " + str(result))
            elif operação == "multiplicação":
                result = multiplicação(num1, num2)
                print("Resultado da multiplicação: " + str(result))
            elif operação == "divisão":
                result = divisão(num1, num2)
                print("Resultado da divisão: " + str(result))
            add_histórico(operação, num1, num2, result)
        elif operação == "histórico":
            print("____Histórico de operações____")
            for item in histórico:
                print(item)
        elif operação == "sair":
            print(".....A sair da calculadora.....")
            break

# Executa a calculadora
calculadora()
