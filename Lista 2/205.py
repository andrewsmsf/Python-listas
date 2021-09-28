#	Faça um programa que peça 20 números inteiros, calcule e 
# mostre a quantidade de números pares e a quantidade de números ímpares.
impar =0
par = 0
count =1
for a in range(1, 21):
    num = int(input("%d - Digite um número: "%a))
    count += 1
    if num %2 == 0:
        par = par + 1
    elif num %1 == 0 :
        impar = impar + 1

print("Foram %d valor(es) impar(es)."%impar)
print("Foram %d valor(es) par(es)."%par)