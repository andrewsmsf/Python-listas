#5.	Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#	A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
#	A mensagem "Reprovado", se a média for menor do que seis;
#	A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

soma = n1 + n2
media = soma/2

if media == 10:
    print('Aprovado com Distinção.')
elif media < 6:
    print('Reprovado.')
elif media >= 6:
    print('Aprovado.')

print('Sua media foi %f' %(media))