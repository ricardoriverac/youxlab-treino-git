#condições
#if- se (estrutura simples)
#else- senão (if/else estrutura composta)
#bloco True e False nunca poderão ser realizados juntos

# tempo= int(input('Quantos anos tem seu carro? '))
# if tempo<=3:
#     print('Carro novo')
# else: 
#   print('Carro velho')
# print('--FIM--')

tempo= int(input('Quantos anos tem seu carro? '))
print('Carro novo >_<'if tempo<=3 else 'Carro velho! -_-')
print('--FIM--')

nome= str(input('Qual é seu nome? '))
if nome=='Alice':
  print('Que nome lindo!')
print('Bom dia, {}!'.format(nome))