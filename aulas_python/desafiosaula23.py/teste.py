try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print('Infelizmente tivemos um problema :( ')
    print(f'O problema foi: \033[31m{erro.__class__}\033[m')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado! ')
    
try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você colocou! ')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero! ')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar os dados! ')
except Exception as erro:
    print(f'O problema foi: \033[31m{erro.__class__}\033[m')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado! ')
