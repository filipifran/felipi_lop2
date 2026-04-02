# Programa para validar string

texto = input("Digite algo: ")

# Verifica se está vazio
if texto.strip() == "":
    print("Dado inválido")
else:
    print(texto)