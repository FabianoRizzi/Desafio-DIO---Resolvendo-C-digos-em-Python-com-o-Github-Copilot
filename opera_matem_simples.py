# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

operacao = input("Digite o número da operação: ")

if operacao == "1":
    resultado = num1 + num2
elif operacao == "2":
    resultado = num1 - num2
elif operacao == "3":
    resultado = num1 * num2
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)
