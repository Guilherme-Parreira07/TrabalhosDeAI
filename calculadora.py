
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


def calculadora():
   num1 = float(input("Digite o primeiro número: "))
   num2 = float(input("Digite o segundo número: "))       
   result = soma(num1, num2)
   print("Resultado da soma: " + str(result))

# Executa a calculadora
calculadora()
