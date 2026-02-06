# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
palavra = input("Digite uma palavra ou frase: ").lower().replace(" ", "")

if palavra == palavra[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
