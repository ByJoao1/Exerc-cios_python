numero = int(input("Digite um número de 4 dígitos: "))

soma_digitos = (numero // 1000) + (numero // 100 % 10) + (numero // 10 % 10) + (numero % 10)

print(f"A soma dos dígitos do número {numero} é: {soma_digitos}")
