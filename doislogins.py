# Programa para validar dois logins

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

# Verificando os dois logins
if (usuario == "atila" and senha == "12345") or (usuario == "olivi" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")