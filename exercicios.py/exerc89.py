from time import sleep
listaNomes = list()
listaNota1 = [ ]
listaNota2 = [ ]
alunos = 0
while True:
    print('-' * 40)
    nomes = input('\033[1mDigite o nome do aluno: \033[m').upper()
    alunos +=1
    nota1 = float(input('\033[1mNota 1 :\033[m '))
    nota2 = float(input('\033[1mNota 2:\033[m '))
    print('-' * 40)
    listaNomes.append(nomes)
    listaNota1.append(nota1)
    listaNota2.append(nota2)
    while True:
        resposta = input('\033[1mQuer continuar?\033[m [S/N] ').upper()
        if resposta in 'SN':
            break
        print('Algo deu errado, tente novamente.', end=' ')
    if resposta == 'N':
        break
print('=-=' *40)
sleep(1)
print('\033[1mBOLETIM FINAL:\033[m ')
print('-' * 40)
sleep(1)
print('\033[2mN°:   NOME:         MÉDIA:\033[m')
for media in range(0, alunos):
    medias = listaNota2[media] + listaNota1[media]
    mediasTotal = medias/2
    print(f'{[media]}   \033[1m{listaNomes[media]:<15}\033[m{mediasTotal:.1f}')

while True:
    qualAluno = int(input('Quer ver as notas de qual aluno? \033[3mdigite 999 para interromper: \033[m'))  
    if 0 <= qualAluno < alunos :
          print(f'As notas de {listaNomes[qualAluno]} foi {listaNota1[qualAluno]} e {listaNota2[qualAluno]}')
    else:
     print('Tente novamente.',end = ' ')

    if qualAluno == 999:
        break