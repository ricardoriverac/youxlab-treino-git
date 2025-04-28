cidade = input('Digite o nome da sua cidade: ')
comecoCidade = cidade.split()
primeiroNome = comecoCidade[0]
if primeiroNome == 'Santo': 
    print('Oba, sua cidade começa com Santo.')
else :
    print ('Aff, sua cidade não começa com Santo.')