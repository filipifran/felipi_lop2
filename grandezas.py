# Programa para cálculo de grandezas elétricas

while True:
    print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
    print("1. Tensão (em Volt)")
    print("2. Resistência (em Ohm)")
    print("3. Corrente (em Ampére)")
    print("4. Sair do programa")

    opcao = input("Qual grandeza deseja calcular? ")

    if opcao == "1":
        # Cálculo da Tensão
        R = float(input("Informe a Resistência (Ohm): "))
        I = float(input("Informe a Corrente (Ampére): "))
        U = R * I
        print(f"Tensão = {U} V")

    elif opcao == "2":
        # Cálculo da Resistência
        U = float(input("Informe a Tensão (Volt): "))
        I = float(input("Informe a Corrente (Ampére): "))
        if I != 0:
            R = U / I
            print(f"Resistência = {R} Ohm")
        else:
            print("Corrente não pode ser zero!")

    elif opcao == "3":
        # Cálculo da Corrente
        U = float(input("Informe a Tensão (Volt): "))
        R = float(input("Informe a Resistência (Ohm): "))
        if R != 0:
            I = U / R
            print(f"Corrente = {I} A")
        else:
            print("Resistência não pode ser zero!")

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")