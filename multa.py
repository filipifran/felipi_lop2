# Programa para calcular multa por excesso de velocidade

# Definindo o limite de velocidade
limite = 80

# Solicitando a velocidade do usuário
velocidade = float(input("Digite a velocidade em Km/h: "))

# Verificando se ultrapassou o limite
if velocidade > limite:
    excesso = velocidade - limite  # Calcula quantos Km/h excedeu
    multa = excesso * 50           # Calcula o valor da multa
    print(f"Limite = {limite} Km/h")
    print(f"Excedeu {excesso} Km/h")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite. Sem multa.")