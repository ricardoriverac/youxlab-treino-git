#preparando território: ESTRUTURA DE REPETIÇÃO WHILE
# resposta= 'S'
# while resposta == 'S':
#     n= int(input('Digite um valor: '))
#     resposta= str(input('Quer continuar?: ')).upper().capitalize()
# print('Fim')

numero= 1
par=impar= 0
while numero != 0:
        numero= int(input('Digite um valor: '))
if numero != 0:
        if numero % 2== 0:
         par += 1
        else:
            impar +=1
print(f'Você digitou {par} números pares e {impar} números ímpares!')