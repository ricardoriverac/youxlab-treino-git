ano = int(input('Digite seu ano de nascimento '))
soma = 2025 - ano

if  soma <= 9:
    print('Você está na categoria MIRIN!!!')

elif soma <= 14:
    print('Você está na categoria INFANTIL!!!')

elif soma  <=19:
    print('Você está na categoria JUNIOR!!!')

elif soma <=20:
    print('Você está na categoria SÊNIOR!!!')

elif soma >20:
    print('Você está na categoria MASTER!!!')

