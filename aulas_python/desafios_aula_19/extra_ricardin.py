calcular = []
print('\033[33m=-=\033[m'*30)
for c in range(0,5):
    nome = str(input('\033[33m-=-=-=-=-=-=-=-=-=-=-\033[m\nQual o nome do aluno?: '))
    media = float(input('Qual a média do aluno?: '))
    calcular.append(media)
soma = sum(calcular)
media = soma / 5
    
if media >= 6:
    print('\033[33m=-=\033[m'*30,f'\nA média da turma está boa, continuem assim..!!\n(Média: {media})')

else:
    print('\033[33m=-=\033[m'*30,f'\nA turma está muito ruim (Média: {media})')
print('\033[33m=-=\033[m'*30)