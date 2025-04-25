
print('Bem vindo ao Goblin Atack!')
enter = str(input('Aperte enter para iniciar'))
esco = int(input('escolha seu personagem: \n 1.Mago \n 2.Bruxa \n 3.Elfo \n 4.Anão \n:'))
nome = str(input('Qual o seu nome?'))


if esco == 1:
    print('Você escolheu o Mago')
if esco == 2:
    print('Você escolheu a Bruxa')
if esco == 3:
    print('Você escolheu o Elfo')
if esco == 4:
    print('Você escolheu a Anão')
while esco >= 5:
    print('Esse persongem não existe')
    esco = int(input('tente novamente'))
else:
    print('agora sim você escolheu o personagem {}'.format(esco))
    print('1. Mago \n 2. Bruxa \n 3. Elfo \n 4. Anão')
    input('Aperte enter para continuar:')
    input('você sai de uma caverna e se depara com uma espada')
    espada = int(input('1: pegar a espada \n 2: Não pegar a espada'))
    if espada != 1:
        input('Você zerou o jogo 👍')
    else:
        input('Você pegou a espada, Aperte enter para seguir em frente')
        input('Essa não, você se deparou com um goblin das montanhas no meio do caminho')
        goblin = int(input('1. Lutar \n 2. Ignorar o goblin'))
        while espada != 1:
            print('Você conseguiu conquistar o goblin, agora ele é seu aliado.')
            input('siga em frente para a bosque')
        else:
            print('Goblin: ♡♡♡♡ \n{}: ♡♡♡♡'.format(nome))
            print('1. Giro mortal 2. Atack básico ')
            n1 = int(input(':'))
            while n1 != 1:
                print('Goblin: ♡♡♡ \n{}: ♡♡♡♡'.format(nome))
                print('1. Giro mortal 2. Atack básico ')
                n1 = int(input(':'))
                

            
    

