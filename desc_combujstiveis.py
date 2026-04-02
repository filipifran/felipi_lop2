# Programa para calcular desconto em combustíveis

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo (A-Álcool / G-Gasolina): ").upper()

if tipo == "A":
    preco_litro = 2.89
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif tipo == "G":
    preco_litro = 4.95
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo inválido!")
    preco_litro = 0
    desconto = 0

valor = litros * preco_litro
valor_final = valor - (valor * desconto)

print(f"Valor a pagar: R$ {valor_final:.2f}")