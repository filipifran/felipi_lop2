# Programa para validar inteiro

entrada = input("Digite um número inteiro: ")

# Verifica se está vazio
if entrada.strip() == "":
    print("Dado inválido")
else:
    numero = int(entrada)
    print(numero)