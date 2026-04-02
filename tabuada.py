# Programa para gerar tabuada

num = int(input("Informe o número da tabuada: "))

# Loop de 1 a 10
for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")