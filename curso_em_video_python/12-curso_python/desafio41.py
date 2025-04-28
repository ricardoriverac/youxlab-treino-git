from time import sleep
print('Olá, seja bem vindo a Confederação Nacional de Natação!')
sleep(1)
print('Para sabermos qual será sua categoria, devemos saber sua idade.')
sleep(1)
print ('PROCESSANDO...')
sleep(2)
ano = int(input('Qual seu ano de nascimento? '))
idade = 2025-ano
if idade <=9 :
    print('Sua categoria será mirim.')
elif idade >9 and idade <=14 :
    print('Sua categoria será infantil.')
elif idade >14 and idade <=19 :
    print('Sua categoria será junior.')
elif idade ==20 :
    print('Sua categoria será sênior.')
elif idade >20 :
    print('Sua categoria será master')
