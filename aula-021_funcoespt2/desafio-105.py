def notas(lista, maior, menor, sit):
    alunos = {}
    for elemento in lista:
        if elemento > maior:
            maior = elemento
            alunos['maior'] = maior
            menor = elemento
        if elemento <= menor:
            menor = elemento
            alunos['menor'] = menor
    media = sum(lista) / len(lista)
    alunos['Média'] = media
    alunos['total'] = len(lista)
    if sit == True:
        if media > 7:
            alunos['situação'] = 'Aprovado'
        elif media < 7:
            alunos['situação'] = 'Reprovado'
    return alunos
        


maior = 0
menor = 0
no1 = []
rang = int(input('Digite o tanto de notas: '))
situ = str(input('Quer ver a situação do aluno? S/N: ')).upper()
if situ == 'N':
    situ = bool(False)
if situ == 'S':
    situ = bool(True)

for c in range(1, rang +1):
    nota = float(input('Digite as notas do aluno: '))
    no1.append(nota)
   

print(notas(no1, maior, menor, sit=situ))