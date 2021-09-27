#4.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido (Utilize elif).

j = 'F'
m = 'M'
questionario = input('Digite F- Femnino ou M - Masculino: ')
if questionario == 'F':
    print('Voce escolheu %s para feminino.'%j)
elif questionario == 'M':
    print('Voce escolheu %s para masculino.'%m)
else :
    print('Alternativa não identificada.')