a = str(input('Digite o que vier no coração e eu falarei quantos "a" tem: ')).strip()
m = ( a[:999].upper())

print('A frase tem essa quantia de "a" : {}'.format ( m.count ('A')))

print ('O primeiro "a" está em: {}'.format (m.find('A')))

print ('O ultimo "a" está em: {}' .format (m.rfind('A')))