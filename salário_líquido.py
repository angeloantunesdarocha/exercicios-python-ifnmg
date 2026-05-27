nome=input("Qual seu nome: ")
salar=float(input("Digite seu salário bruto: "))
print()
ir=float(salar*0.11)
inss=float(salar*0.08)
sind=(salar*0.05)
if salar >= 5000:
    liq1=salar-ir-inss-sind
    print(nome,",Os valores descontados são:\n\nR$",ir,"(imposto de renda)\nR$",inss,"(INSS)\nR$",sind,"(Contribuição Sindical)\n\nRestou R$",liq1,"(de salário liquido!)")
else:
    liq1=salar-inss-sind
    print(nome,",Os valores descontados são:\n\nR$ 0 (imposto de renda isento)\nR$",inss,"(INSS)\nR$",sind,"(Contribuição Sindical)\n\nRestou R$",liq1,"(de salário liquido!)")
    
