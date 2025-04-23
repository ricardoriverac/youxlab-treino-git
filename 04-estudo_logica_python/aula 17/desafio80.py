
lista=[]

 

for i in range(0,5):
 

    numero=int(input('Digite um valor:'))
 

    if i == 0 or numero> lista[-1]:
 

        lista.append(numero)
 

        print('ADICIONADO NA LISTA')
 

    else:
 

        posiçao=0
 

        while posiçao < len(lista):
 

           if numero<= lista[posiçao]:
 

              lista.insert(posiçao, numero)   
 

              #print(f'foi adicionado na posiçao {posiçao}')
 

              break
 

           posiçao+= 1
 


 

print(f' os valores digitados em ordem sao{lista}')            
 

        

  