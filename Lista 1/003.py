#3.	Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

n1 = int(input("Digite um valor inteiro: "))

if n1 % 2 ==0:
    print("O valor %d é par."%(n1))
elif n1 % 1 == 0:
    print("O valor %d é impar."%(n1))
