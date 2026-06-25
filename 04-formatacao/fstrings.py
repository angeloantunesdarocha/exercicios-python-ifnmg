# Mostrando valores na tela
print("Olá mundo!")

# nome = input("Qual é seu nome? ")
# print("Boa noite", nome)

x = 98
y = 74
resultado = x + y

# Temos outras formas de mostrar variáveis na tela em Python.
print(x, "+", y, "=", resultado)  # Forma padrão
print("%s + %s = %s" % (x, y, resultado))  # Usando o operador %
print("{} + {} = {}".format(x, y, resultado))  # Usando o método .format
print(f"{x} + {y} = {resultado}")  # Usando f-strings

# Podemos fazer operações diretamente nas strings.
print(f"{x} + {y} = {x + y}")

# Podemos formatar datas.
dia = 1
mes = 6
ano = 2026

print(f"{dia}/{mes}/{ano}")
print(f"{dia:02d}/{mes:02d}/{ano}")

# Podemos formatar números decimais.
valor = 66.397234
print(f"Valor R$ {valor}")
print(f"Valor R$ {valor:.2f}")
print(f"Valor R$ {valor:.3f}")

# Podemos imprimir valores como porcentagens.
desconto = 0.10
valor_final = valor * (1 - desconto)

print(
    f"Valor do produto R$ {valor:.2f}, "
    f"desconto {desconto:.1%}, "
    f"valor final R$ {valor_final:.2f}"
)

# Controlando a posição dos elementos na string.
print(f"|{'início':<30}|")
print(f"|{'meio':^30}|")
print(f"|{'fim':>30}|")

# Podemos formatar números binários.
numero = 1245
print(f"Número em base decimal: {numero}. Número em binário: {numero:b}")

numero_binario = "1010110"
print(
    f"Número em base decimal: {int(numero_binario, 2)}. "
    f"Número em binário: {numero_binario}"
)

# Podemos usar condicionais dentro das f-strings.
nota = int(input("Digite a nota do aluno: "))
print(f"Você foi {'aprovado' if nota >= 60 else 'reprovado'}.")
