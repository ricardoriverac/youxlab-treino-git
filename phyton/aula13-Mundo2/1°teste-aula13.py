for contador in range(0,6):#Se for (1,6) aparecerá 5 'oi!' pois n inicia a contagem do zero 
    print('Oi!')
print('FIM')


print('CONTANDO DE 1 À 6')
for contador in range(1,7):
    print(contador)
print('FIM')


print('CONTAGEM REGRESSIVA 0 À 6')
for contador in range(6,0,-1):
    print(contador)
print('FIM')


print('CONTAGEM de 2 EM 2 ATÉ 6')
for contador in range(0,7,2):
    print(contador)
print('FIM')


print('CONTADOR DE 0 ATÉ NÚMERO ESCOLHIDO')
numero=int(input('Digite um número:'))
for contador in range(0,numero+1):
    print(contador)
print('Fim')
print('CONTADOR DE PASSOS')


inicio=int(input('Digite o início das plataformas:'))
fim=int(input('Digite onde as plataformas acabam:'))
passos= int(input('Quantidade de passos:'))
for contador in range(inicio,fim+1,passos):
    print(contador)
print('Fim')

   
print('PEDINDO VALORES 3 VEZES')
for contator in range(0,3):
    numero=int(input('digite um número:'))
print('fim')


print('SOMANDO VALORES')
soma=0
for contator in range(0,3):
    numero=int(input('digite um número:'))
    soma=soma+numero
print(f'A soma dos 3 n° é:{soma}')

