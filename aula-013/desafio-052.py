#def eh_primo(numero):
    #if numero < 2:
        #return False  # Números menores que 2 não são primos

    #for i in range(2, int(numero ** 0.5) + 1):  # Verifica divisores até a raiz quadrada do número
        #if numero % i == 0:
            #return False  # Se encontrar um divisor, não é primo

    #return True  # Se não encontrou nenhum divisor, é primo

# Entrada do usuário
#num = int(input("Digite um número: "))

# Verificação e saída do resultado
    #print(f"{num} é um número primo!")
#else:
    #print(f"{num} não é um número primo.")

#num = int(input('Digite um número'))
#for c in range(1, num + 1):
    #if num % c == 0:
        #print('\033[34m', end='')
    #else:
        #print('\033[m')
    #print('{} '.format(c), end='')
        
#num = int(input('Digite um numero'))
#n = 0
#for c in range(1, num + 1):
    #if num % c == 0:
        #n += 1
        #print('\033[33m', end=' ')
    #else:
        #print('\033[31m', end= ' ')
    #print('{}'.format(c), end= ' ')
#print('\n O número {} foi dividido {} vezes'.format(num, n))

num = int(input("digite um valor:"))
for c in range(1, num +1):
    if num % c ==0:
        print(c)
    else:
        print('false')
    
