# Programa para calcular desconto da Black Friday

preco = float(input("Digite o valor da compra: "))

print("Formas de pagamento:")
print("1 - À vista (10%)")
print("2 - Débito (5%)")
print("3 - Crédito (3%)")
print("4 - PIX (7.5%)")

opcao = int(input("Escolha a forma de pagamento: "))

# Aplicando desconto
if opcao == 1:
    desconto = 0.10
elif opcao == 2:
    desconto = 0.05
elif opcao == 3:
    desconto = 0.03
elif opcao == 4:
    desconto = 0.075
else:
    desconto = 0
    print("Opção inválida!")

valor_final = preco - (preco * desconto)

print(f"Valor final: R$ {valor_final:.2f}")