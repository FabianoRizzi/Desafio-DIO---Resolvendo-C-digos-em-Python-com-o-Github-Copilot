# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

texto = input("Digite uma palavra ou frase: ")
numero = int(input("Digite um número inteiro: "))

resultado = (texto + " ") * numero
print(resultado)
