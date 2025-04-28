num = int(input('digite o número da tabuada que você quer saber. '))
for c in range(1 , 11):
    print('{} . {:2} = {}'.format(num, c, num*c))