#	Faça um Programa que peça dois números e imprima o menor deles.

n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))

if (n1 < n2):
    print("O numero "+str(n1)+" é o menor")
elif (n2 < n1) :
   print("O numero "+str(n2)+" é o menor")
else:
    print("Os dois são iguais.")