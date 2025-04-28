#Forma básica do try
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente tivemos um problema :(')

# else:  # Colocando o else não aparece a mensagem feia de erro e sim só a do except
#     print(f'O resultado é {r}')

# finally: # Sempre vai acontecer independente se o programa der certo ou não
#     print('Volte sempre! Muito obrigada!')

# #Mostrando qual foi o erro
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b

# except Exception as erro: # é útil pra saber oq tá errado quando tiver programando
#     print(f'Problema encontrado foi {erro.__class__}') # tem várias opções q podem ser mostradas no lugar do class

#Vários except dentro do try
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
    
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre! Muito obrigada!')
