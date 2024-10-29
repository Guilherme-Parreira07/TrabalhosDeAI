
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

#Função principal
def calculadora():
    while True:
        operação = input ("Escolha a operação: ")
        if operação == "subtração":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = subtração(num1, num2)
            print("Resultado da subtração: " + str(result))
        elif operação == "soma":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = soma(num1, num2)
            print("Resultado da soma: " + str(result))
        elif operação == "multiplicação":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = multiplicação(num1, num2)
            print("Resultado da multiplicação: " + str(result))
        elif operação == "divisão":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = divisão(num1, num2)
            print("Resultado da divisão: " + str(result))
        elif operação == "sair":
            print(".....A sair da calculadora.....")
            break

# Executa a calculadora
calculadora()
