def leInt(n):
    while True:
        numero = input(n)
        try:
            numero = int(numero)
            print(f'Você digitou o número {numero}')
            return numero
        except ValueError:
            print(print('Erro: Você não digitou um número inteiro válido.'))
            
        
    
            

n = leInt('Digite um número: ')
print(f'Número recebido: {n}')