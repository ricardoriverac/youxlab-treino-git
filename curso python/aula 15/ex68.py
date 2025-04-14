from random import randint
itens = ['impar', 'par']
print ("\t_=_" * 20)
print ("VAMOS JOGAR PAR OU ÍMPAR... ")
print ("\t_=_" * 20)
while True : 
    computador = randint (0,10)
    jogador = str (input ("Digite um número: "))
    print ("Compuador jogou: \033[33m{}\033[m ".format(itens[computador]))
    print ("Jogador jogou: \033[34m{}\033[m ".format(itens[jogador]))