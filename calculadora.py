
# Função para subtração
def subtração(x, y):
    return x - y

#Função para soma
def soma(x, y):
    return x + y

#Função para multiplicação
def multiplicação(x, y):
    return x * y

#Função para divisão
def divisão (x, y):
    return x / y

# Função principal
def calculadora():
    operador = input ("Escolha a operação: ")
    if operador == "subtração":
        num1 = int(input("Digite o segundo número: "))
        num2 = int(input("Digite o segundo número: "))
        result = subtração(num1, num2)
        print("Resultado da subtração: " + str(result))
    if operador == "soma":
        num1 = int(input("Digite o segundo número: "))
        num2 = int(input("Digite o segundo número: "))
        result = subtração(num1, num2)
        print("Resultado da soma: " + str(result))
    if operador == "multiplicação":
        num1 = int(input("Digite o segundo número: "))
        num2 = int(input("Digite o segundo número: "))
        result = subtração(num1, num2)
        print("Resultado da multiplicação: " + str(result))
    if operador == "divisão":
        num1 = int(input("Digite o segundo número: "))
        num2 = int(input("Digite o segundo número: "))
        result = subtração(num1, num2)
        print("Resultado da divisão: " + str(result))

# Executa a calculadora
calculadora()
