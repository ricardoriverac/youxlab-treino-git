feminino = 'F'
masculino = 'M'
r = 0
while r != feminino and r != masculino:
    r = input('Qual seu sexo? [F/M]: ').upper()
    if r != 'M' and r != 'F':
        print('Digite uma resposta válida')