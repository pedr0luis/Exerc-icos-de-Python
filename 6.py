V = float(input("Valor recebido por hora: R$"))
H = int(input("Horas trabalhadas no mês:"))
B = V*H
print("Salário bruto: R$%.2f"%B)
IR = B*0.11
print("Imposto de Renda é R$%.2f"%IR)
INSS = B*0.08
print("INSS: R$%.2f"%INSS)
S = B * 0.05
print("Sindicato: R$%.2f"%S)
print("Salário liquido: R$%.2f"%(B - (IR + INSS + S)))
