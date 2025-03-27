n1 = float(input('Primeira nota:'))
n2 = float(input('Segundo nota: '))
media = (n1 + n2) / 2 
print(f'O aluno que tirou {n1} e {n2} terá sua média de {media}')
if media < 5 : 
    print('Este aluno está REPROVADOO')
elif media >= 5 and media < 7 :
    print('Este aluno está de RECUPERAÇÃO')
elif media >= 7 :
    print('Este aluno está APROVADO')