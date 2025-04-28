def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))

        except (ValueError, TypeError):
            print(' \033[31mErro:por favor, digite um numero inteiro valido \033[m')

        except (KeyboardInterrupt):
            print('Entrada de dados interrompidos pelo usuario ')
            
        else:
            return n
        


numero = leiaInt('Digite um número: ')
print(f'O valor digitado foi {numero}')
