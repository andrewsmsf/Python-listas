#7.	Faça um programa que imprima na tela apenas os números ímpares entre dos valores recebidos.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
maxi = 0
menor =0

if (n1 < n2):
    menor = n1
    maxi = n2
else : 
    menor = n2
    maxi = n1

for i in range(menor + 1, maxi):
    if i %2 != 0:
        print(i)
