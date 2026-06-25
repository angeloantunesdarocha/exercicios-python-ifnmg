numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if numero_2 != 0:
    divisao = numero_1 / numero_2
    print(f"Divisão: {divisao}")
else:
    print("Não é possível dividir por zero.")
