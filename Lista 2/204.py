#4.	Faça um programa que peça dois números, base e expoente, calcule 
# e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
n1 = int(input("Informe um número para a base: "))
n2 = int(input("Informe o segundo número para o expoente: "))

bas = 1
for x in range(n2):
    bas = n1*bas
    x += 1
print("A base é: %d"%n1)
print("O expoente é: %d"%n2)
print("Resultado de "+str(n1)+" elevado a "+str(n2)+" é: "+str(bas))