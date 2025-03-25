nome = input('Qual é o seu nome? ')
#print('Opa, {}! Aceita um cafézin?'.format(nome))
print(f'Opa, {nome}! Aceita um cafézin?')

print('Ei, se importa de falar seu aniversário? é pro meu TCC')

data = input('Data: ')
mes = input('Mês: ')
ano = input('Ano: ')
print(f'Então o seu dia do bolo é dia {data} de {mes} de {ano}, certo?')

print('Beleza, vamos fazer um negócio bacana aqui')
#int() converte uma string para um número inteiro
a = int(input ('Escolhe um número: '))
b = int(input ('Ótimo! Agora escolhe outro: '))
soma = a + b
# print(f'A soma de {a} + {b} é {soma}')
print('A soma de', a, '+', b, 'é',  soma)