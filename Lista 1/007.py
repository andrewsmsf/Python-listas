#7.	Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido

n1 = int(input('Escreva um numero: '))
semana = ['sla', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

if n1 <= 7 and n1 > 0:
    print('O número '+str(n1)+' representa '+ semana[n1])
else:
    print('Número inválido')