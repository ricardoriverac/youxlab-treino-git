contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('O valor digitado é inválido! Tente novamente.')
    else:
        print(f'O número por extenso é: {contagem[num]}')
    resp = str(input('Executar novamente? [S/N]: ')).upper().strip()[0]
    if resp not in 'S':
        break
print('Programa finalizado.')