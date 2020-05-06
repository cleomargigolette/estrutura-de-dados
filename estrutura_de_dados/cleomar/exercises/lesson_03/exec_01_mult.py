num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

def multiplicacao(num1, num2):
    resultado = 0
    for i in range(num2):
        resultado += num1
    return resultado

print(multiplicacao(num1, num2))