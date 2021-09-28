#1.	Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
n1 = int(input("Digite um valor de 0 a 10: "))

while n1 >= 0 and n1 <= 10:
    n1 = int(input("Digite um valor de 0 a 10: "))

print('Valor inválido.')