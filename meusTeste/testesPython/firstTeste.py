listaAnalistas= ['intp', 'istp', 'entp', 'entj']
listaSentinelas= ['istj', 'estj', 'isfj', 'esfj']
listaDiplomatas= ['infp', 'infj','enfj', 'enfp']
listaExploradores = ['estp', 'istp', 'esfp', 'isfp']
mbti = ''
print('VAMOS DESCOBRIR SEU MBTI')

while True:
    print('Eu sou:')
    print('[1] Introvertido')
    print('[2] Extrovertido')
    IouE = int(input('Você é INTROVERTIDO ou EXTROVERTIDO? '))
    if IouE == 1 and IouE ==2:
        break
    print('Digite certo.', end='')
    break
if IouE == 1:
    mbti = 'i'
else:
    mbti = 'e'

print(mbti)

