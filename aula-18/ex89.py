boletim = []
indv = []
while True:
    alunos = int(input('Deseja registrar o boletim de quantos alunos? '))
    for p in range(alunos):
        alunos.append([p])
        for n in range(p):
            notaUm = int(input('Primeira nota:'))
            indv.append(notaUm[n])        
            notaDois = int(input('Segunda nota'))
            indv.append(notaDois[n])
            media = notaUm + notaDois 
    break
print(indv)