#2.	Faça um programa que leia 5 números e informe a soma e a média dos números
n1= 1
num =0
soma= 0
for a in range(5):
    num += int(input("Digite o %dº numero: "%(n1)))
    n1 += 1
media = num/5
print("A soma é %d"%(num))
print("A media foi %d. "%(media))