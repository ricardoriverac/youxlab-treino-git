soma = 0
quantidade = 0
maximo = 0 
nomev = ''
contadorf = 0

for c in range(1,5):
    print(F'----- {c}ª PESSOA -----')
    nome = str(input('Qual seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    soma += idade
    quantidade += 1
    media = soma / quantidade
    
    if c == 1 and sexo in 'mM':
        maximo = idade
        nomev = nome
        
    if sexo in 'Mm' and idade > maximo:
            maximo = idade
            nomev = nome
    
    if sexo in 'Ff' and idade < 20:
          contadorf += 1
        
        
 
print(F'\nA média de idade do grupo é de {media} anos')
print(F'O homem mais velho tem {maximo} anos e se chama {nomev}')
print(F'ao todo são {contadorf} mulheres com menos de 20 anos')


      
