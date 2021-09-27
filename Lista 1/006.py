#6.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
#  desenvolver o programa que calculará os reajustes.
#	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#	salários até R$ 280,00 (incluindo) : aumento de 20%
#	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# salário antes do reajuste;
# percentual de aumento aplicado;
# valor do aumento;
# novo salário, após o aumento.

salario = float(input('Digite seu salário: '))

if salario <= 280:
    aumento = (salario * 0.20) + salario
    percentual = aumento - salario
    print('Salário antes do ajuste R$%.2f'%(salario))
    print('Aumentou 20%.')
    print('Valor do aumento foi R$%.2f'%(percentual))
    print('Salário ajustado R$%.2f'%(aumento))
elif salario > 280 and salario <= 700:
    aumento = (salario * 0.15) + salario
    percentual = aumento - salario
    print('Salário antes do ajuste R$%.2f'%(salario))
    print('Aumentou 15%.')
    print('Valor do aumento foi R$%.2f'%(percentual))
    print('Salário ajustado R$%.2f'%(aumento))
elif salario > 700 and salario <= 1500:
    aumento = (salario * 0.10) + salario
    percentual = aumento - salario
    print('Salário antes do ajuste R$%.2f'%(salario))
    print('Aumentou 10%.')
    print('Valor do aumento foi R$%.2f'%(percentual))
    print('Salário ajustado R$%.2f'%(aumento))
elif salario > 1500:
    aumento = (salario * 0.05) + salario
    percentual = aumento - salario
    print('Salário antes do ajuste R$%.2f'%(salario))
    print('Aumentou 5%.')
    print('Valor do aumento foi R$%.2f'%(percentual))
    print('Salário ajustado R$%.2f'%(aumento))