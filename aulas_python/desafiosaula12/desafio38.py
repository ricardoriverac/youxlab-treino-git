primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
if primeiroNumero>segundoNumero:
    print('O primeiro valor é maior que o primeiro ')
elif segundoNumero>primeiroNumero:
    print('O segundo valor é maior que o primeiro ')
elif primeiroNumero == segundoNumero:
    print('Não existe valor maior, os dois são IGUAIS ')
