# Programa que lê cinco números e exibe

numeros = []

# Loop para ler 5 números
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Exibindo os números
print("Números digitados:")
for n in numeros:
    print(n)