#  variavéis compostas TUPLAS
#  print (lanche[2]) fateamento, do único elemento dessa posição
#  print (lanche[0:2]) fateamento, o dois não é mostrado
#  print (lanche[1:]) fateamento, do elemento 1 até o fim da última posição
#  print (lanche[-1]) fateamento, elemento de trás pra frente (começa na última posição)
# len(lanche) COMPRIMENTO, quantos elementos tem
#  for c in lanche:
#       print(c) > imprime o primeiro elemento da posição, quando faz o loop ele imprime os outros elementos, até chegar ao fim
#              AS DUPLAS SÃO IMUTÁVEIS

#           começa em 0 ......
lanche = ('hambúrguer', 'suco', 'pizza' , 'pudim' )
print(lanche) # imprime TODOS os elementos
print (lanche[1]) # imprime elemento 1, suco
print (lanche[3]) # imprime elemento 3, pudim
print (lanche[-2]) # imprime elemento - 2, pizza , trás para frente
print (lanche[1:3]) # imprime elemento 1 e 3, suco e pizza , FATEAMENTO desconsidera o último elemento
print (lanche[2:]) # imprime elemento 2 (piza) até FIM (pudim)
print (lanche[:2]) # imprime do PRIMEIRO (hambúrguer) elemento até o elemento 2 suco
print (sorted(lanche)) # mostra os elementos em ordem
# print formatado
for comida in lanche:
    print (f"Eu vou comer {comida}") # TIPOS
print (len(lanche)) # QUANTIDADE
print ("comi pra caramba!")

a = (2, 5 , 4)
b = (5,8,1,2)
c = b + a # vai ter os números da tupla b + a
print (a)
print (b)
print (c)
print (len(c)) # quantidade de elementos
print (c.count(5)) # quantas vezes aparece o número 5
print (c.index(8)) # posição do número 8
print (c.index(5 , 1)) # posição do número 5 que aparece duas vezes
# DEL APAGA
