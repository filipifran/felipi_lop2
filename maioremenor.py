# Programa que lê três números e mostra maior, menor, soma e média

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calculando valores
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
soma = num1 + num2 + num3
media = soma / 3

# Exibindo resultados
print("**********")
print(f"Maior = {maior}")
print(f"Menor = {menor}")
print(f"Soma = {soma}")
print(f"Média = {media}")