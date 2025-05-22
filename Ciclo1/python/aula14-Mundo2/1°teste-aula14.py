print('1° TESTE')
contador=1
while contador<10: #enquanto contador for menor que 10 some 1 ao contador
    print(contador, end=' ')
    contador+=1 #soma
print('FIM!')

print('2° TESTE')
numero=1
while numero!=0:#enquanto valor NÃO for 0 repete a sequência
    numero=int(input('Digite um n°:'))
print('FIM!')

print('3° TESTE')
resposta='SIM'
while resposta=='SIM':
     numero=int(input('Digite um n°:'))
     resposta=str(input('Quer continuar? Sim/Não:')).upper
print('FIM!')

print('4° TESTE')
numero=1
par= impar= 0
while numero!=0:#enquanto valor NÃO for 0 repete a sequência
    numero=int(input('Digite um n°:'))
    if numero % 2 ==0:
        par+=1
    else:
        impar+=1
print(f'Você digitou {par} números pares e {impar} números impares')