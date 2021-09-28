#8.	(Desafio) Faça um programa que apresenta a tabuada completa de 1 a 10.
n1=0
while n1<10:
    n1+=1 
    n2=0
    print("\n")
    while n2<10:
        n2+=1
        resultado = n1*n2
        print("Tabuada %s x %s = %s"%(n1,n2,(resultado)))
