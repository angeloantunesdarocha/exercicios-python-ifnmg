nome=input("Digite seu nome: ")
dias=int(input("Digite quantos dias: "))

ano=dias//365
resto=dias%365
meses=resto//30
dias_finais=resto%30

print(nome,",você digitou",dias,"dias, que equivalem a =>",ano,"ano(s),",meses,"mes(es) e",dias_finais,"dia(s)\nAté a próxima!")

