valores=[]

for numero in range(0,5):

    valores.append(int(input('Me diga um valor: ')))

    if numero ==0:
        maior=menor= valores[numero]
       
    elif valores[numero] >maior:
         maior = valores[numero]

    elif valores[numero] < menor:
        menor = valores[numero]

    for posicao,valor in enumerate(valores):
        if valor == maior:
            maiorP = posicao

        if valor == menor:
            menorP = posicao

print(f'O maior valor e {maior} e ta na posição {maiorP} ')
print(f'O menor valor e {menor} e ta na posição {menorP}')




# print(f'O maior número e {maior} e incontrei na posição {posicao}')

# print(f'O menor valor e {menor} e esta na posição ')









# for posicao,valor in enumerate(valores):

#     print(f'Na posição {posicao} temos o valor {valor}')

#     print(f'Como maior valor temos {max(valores)} digitado na posição {posicao}')

#     print(f'O menor valor e {min(valores)} digitado na posição {posicao} ')