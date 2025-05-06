#   FUNÇÕES PARTE 2
#   INTERACTIVE HELP
#   help()
# '''print('ola, mundo')
#help(print)''' # explica a funcionalidade do comando
#   DOCSTRINGS
#def contador(i,f,p):

#  """
# -> FAÇA UMA CONTAGEM E MOSTRE NA TELA:
#    param i: inicio da contagem
#    param f: fim da contagem
#  param p: passo da contagem
#   return: sem retorno
#   """
#    c = i
#   while c <= f:
#       print (f'{c}', end='')
#       c += p
#   print('fim')
# help(contador)
# parâmetos opcionais
# def somar(a=0,b=0,c=0):
#   s = a + b + c
#   print (f'A soma vale: {s}')
#somar(3,2,5)
#somar(8,4)
#somar()
#   escopo de uma variavél
#def teste():
#    x = 8
#    print (f'Na função teste n, vale {n}')
#   print (f'Na função teste, x vale {x}') # X é variavél local
#n = 2
#print (f'Na função principal n , vale {n}') # N é variavél global
#teste()
#def somar(a=0,b=0,c=0):
#   s = a + b + cprint(lanche)
#   return s
#r1=somar(3,2,5)
#r2=somar(8,4)
#r3=somar(6)
#print (f'Os resultados foram: {r1}, {r2} e {r3}.')