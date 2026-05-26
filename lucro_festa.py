visit=int(input("Digite quantos visitantes: "))
ingres=float(input("Digite valor de cada ingresso: "))
alimen=float(input("Quanto de alimentação por visitante: "))
mult1=ingres*visit
mult2=visit*alimen
sub=ingres-alimen
print("Total de receita é: ",mult1)
print("Total de gasto com alimentação é: ",mult2)
print("Total líquido é: ",sub)