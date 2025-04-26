def fatorial(numero, show=False):
        """
    Calcula o fatorial de um número.

    Parâmetros:
    numero (int): O número para calcular o fatorial.
    show : Se True, exibe o cálculo passo a passo. O padrão é False.

    Retorna:
    None: A função não retorna nada, mas pode imprimir o cálculo dependendo do valor de 'show'.

    Exemplo de uso:
    fatorial(5, show=True)  # Exibe o cálculo passo a passo.
    fatorial(5)             # Apenas calcula o fatorial, sem exibir o cálculo.
    """
    
        if show:
            counter = numero 
            fatorar = 1 
            print('Calculando...{}! =\n'.format(numero), end='')
            while counter > 0:
                print('{}'.format(counter), end='')
                fatorar *= counter
                counter -= 1
                print(' x ' if counter > 0 else ' = ', end='')
            print('{}'.format(fatorar))
    
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f'O fatorial de {numero} é: {fatorial}')
        
# numero = int(input('Digite um número e descubra o seu fatorial: '))
# # ou a funcionalidade abaixo :)
# print(fatorial(5, True))
print(help(fatorial))