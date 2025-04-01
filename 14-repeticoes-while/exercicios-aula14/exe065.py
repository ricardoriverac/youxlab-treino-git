resp = 'S'
soma = 0
quantidadedeNumeros = 0
media = 0
maior = 0 
menor = 0
while resp in 'Ss' :
    num = int(input('Digite um número: '))
    soma = soma + num 
    quantidadedeNumeros = quantidadedeNumeros + 1
    if quantidadedeNumeros == 1:
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor :
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
media = soma/quantidadedeNumeros
print(f'Você digitou {quantidadedeNumeros} números é a soma entre foi {soma}')
print(f'A media dos números digitados foi {media:.1f}')
print(f'O maior valor digitado foi {maior} é o menor foi o {menor}')


