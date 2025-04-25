print('1° TESTE:')
numeros=[2,4,6,8]  #listas são sempre em colchetes
numeros[2]=5   #n° na posição 2 será substituido pelo n°5
print(numeros)

print('2°TESTE:')
numeros=[3,6,5,7]
numeros.append(2)  #Adiciona o n°2 na lista 
print(numeros)

print('3°Teste:')
numeros=[3,8,4,6,1]
numeros.sort()  #coloca os n° de ordem crescente
print(numeros)
numeros=[3,8,4,6,1]
numeros.sort(reverse=True) #coloca os n° em ondem decrescente
print(numeros)

print('4°TESTE:')
numeros=[1,2,3,4]
print(f'Nesta lista tem {len(numeros)} elementos') #mostra quantos elementos hà na lista

print('5°TESTE:')
numeros=[5,6,7,4]
numeros.insert(1,2) #ADICIONA um elemento, neste caso na posição 1 foi adicionado o n°2
print(numeros)

print('6°TESTE:')
numeros=[1,4,3,2]
numeros.pop()  #retira o ÚLTIMO elemento da lista
print(numeros)
numeros=[1,4,3,2]
numeros.pop(2)  #elimina o elemento da posição 2, no caso o n°3 
print(numeros)

print('7°TESTE')
numeros=[9,7,4,2]
numeros.insert(8,1)
print(numeros)

print('8°TESTE')
numeros=[9,8,7,6,9]  
numeros.remove(9)  #remove somente o 1° 9 que aparece
print(numeros)

print('9°TESTE')
numeros=[3,7,8,4] 
if 8 in numeros:  #se tiver n°8 na lista de números irá ser removido
    numeros.remove(8) 
else:  #se não tiver escreva
    print('Não tem esse n° na lista')
print(numeros)
