nome = str(input('Digite seu nome completo: ')).strip()
sm = len(nome) - nome.count(' ')
nf = nome.find(' ')
print(f'Seu nome em maiúsculas {nome.upper()}')
print(f'Seu nome em minúsculas {nome.lower()}')
print(f'Ao todo seu nome tem {sm} letras')
print(f'Seu primeiro nome tem {nf} letras')

