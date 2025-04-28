ano = int(input('Qual o seu ano de nascimento? '))
anoAlistar = 2025-ano
tempo = 18 - anoAlistar
if anoAlistar ==18 :
    print('Já está na hora de se alistar ao serviço militar.')
elif anoAlistar <18 :
    print('Você ainda irá se alistar ao serviço militar. Faltam {} anos.'.format(tempo))
elif anoAlistar >18 :
    print('Já passou da hora de você se alistar ao serviço militar!!! Você está atrasado por {} anos!'.format(tempo))
    