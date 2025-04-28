valores=[]
while True:
    resposta =str(input('Deseja continuar [S/N]: ').upper())

    if resposta == 'N':
        break

    valor =int(input('Me diga um número para ser adicionado em valores: '))
    valores.append(valor)

if 5 in valores:
    print('O número 5 foi digitado ')

else:
    print('Nada do cinco ')

print(f'{len(valores)}')
print(sorted(valores))    



