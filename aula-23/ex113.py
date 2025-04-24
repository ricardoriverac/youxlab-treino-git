# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31mERRO! Digite um número inteiro.\033[m ')
#         if ok:
#             break
#     return valor
def leiaInt(pergunta):

    valorB = 0
    while True:
        try:
            n = input(pergunta)
        
            valorB = int(n)
          
            break
        except (ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido')
            
        except KeyboardInterrupt:
            print('Usuário preferiu não informar o valor')
        except Exception as erro:
            print(f'O erro é {erro.__cause__}')
      
    return valorB

def leiaFloat(msg):
    valorF = 0
    while True:
        try:
            n = input(msg)
            valorF = float(n)
            break

        except (ValueError, TypeError):
            print('ERRO: Digite um número real válido')
            
        except KeyboardInterrupt:
            print('Usuário preferiu não informar o valor')
    return valorF

a = leiaInt('Digite um número inteiro: ')
b = leiaFloat('Digite um número real: ')
print(f'O número inteiro é {a} e o real é {b}')