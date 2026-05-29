print()
nome=input("Qual o seu nome? ")
print()
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
print()
if num1>num2:
    maior=num1
    resto=maior-num2
    print(nome,", o maior número é",maior,"\nA diferença é",resto)
    print()
    print("FIM DO ALGORITMO!")
    print()
else:
    print()
    maior=num2
    resto=maior-num1
    print(nome,", o maior número é",maior,"\nE a diferença é",resto)
    print()
    print("FIM DO ALGORITMO!")
    print()