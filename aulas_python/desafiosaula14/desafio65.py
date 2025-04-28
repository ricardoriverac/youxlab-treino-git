numero = contador = soma = maior = menor = media = 0
usuarioQuerContinuar = ''
while usuarioQuerContinuar !='N' or usuarioQuerContinuar == 'S':
    numero = int(input('Digite um valor: '))
    usuarioQuerContinuar = input('Você deseja continuar a digitar valores?{}[S/N]{}: '.format('\033[33m', '\033[m')).upper()
    if contador==0:
        menor = numero
    soma+=numero
    contador+=1
    if numero>maior:
        maior = numero
    if numero<menor:
        menor = numero
    if usuarioQuerContinuar == 'N':
        print('ACABOU')
media = soma/contador
print('A {}SOMA{} dos números é {} e a {}MÉDIA{} é {:.2f} '.format('\033[35m', '\033[m',soma, '\033[35m', '\033[m', media))
print('O {}MAIOR{} número é {} e o {}MENOR{} {} '.format('\033[35m', '\033[m', maior, '\033[35m', '\033[m', menor))


