#for c in range(1, 10):
    #print(c)
    #if c == 2:
        #print('o numero {} foi ignorado'.format(c))
    #print(c)

#tabuada
#num = int(input("Digite um número:"))
#for c in range(1,11):
    #print(num * c)

#façã um programa que pergunte ao usuario um numero e retorne a soma desse numero + 1
#num = int(input('Digite um número:')) #pergunta ao usuario um numero
#for c in range(1, num): #vai definir o range e tanto de vezes que o numero sera somado por 1
    #print(c + num) #vai mostrar a a soma do numero mais 1 de cada numero do 1 até numero que o usuario colocou

#faça um programa que impima numeros pares dentro de unm range de 1 até 20

#for c in range (1, 21):
    #a = (c % 2)
    #if a == 0:
        #print('o {} é par'.format(c))

#contagem regressiva usando o time para mostrar a contagem.

#import time

#for c in range(10, -1, -1):
    #time.sleep(1)
    #print(c)

# import random
# num = random.randint(1, 10)
#jogador = int(input('Advinhe um número:'))
#while jogador != num:
    #print('Errou, tente de novo')
    #jogador = int(input('Advinhe um número:'))
#else:
    #print('Você acertou')

# for c in range(1, 11):
#     while num != c:
#         print('Errou tente de novo')
#         print (num)
#     else:
#         print('Você acertou!')

homens = []

while True:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    if sexo == 'M':
        homens.append({'nome': nome, 'idade': idade})

    continuar = input("Deseja adicionar outra pessoa? (S/N): ").strip().upper()
    if continuar != 'S':
        break

print("\nLista de homens cadastrados:")
for homem in homens:
    print(f"{homem['nome']} - {homem['idade']} anos")
