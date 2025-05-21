try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou;')
else:
    print(f'a{r:.1f}')
    
finally:
    print('Volte sempre')