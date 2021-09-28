#6.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Escolha um número: '))
resposta = 1
print('{}!='.format(num), end = '')

while (num >= 1):
    if (num == 1):
       print('{}'.format(num), end = '')
    else:
       print('{}'.format(num), end = '')
    resposta = resposta * num
    num -= 1
print('={}'.format(resposta))