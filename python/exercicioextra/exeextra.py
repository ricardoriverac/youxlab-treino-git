nome = str(input('Digite seu nome: '))
saldo_inicial =  float(input('Saldo que você contem: '))
limite_saque = float(input('Limite de saque que você quer fazer:  '))
Saldo_Adicionado = saldo_inicial
totdepositado = list()
totsaque = list()
while True:
    print("""
          [1] Consultar saldo 
          [2] Depositar valor 
          [3] Sacar valor
          [4] Ver extrato 
          [5] Sair
          """)
    opcao = int(input('Digite as opcões: '))
    if opcao == 1 :
        print(f'Seu saldo atual até agora é {Saldo_Adicionado:.2f}')
    if opcao == 2 :
        depositar = int(input('Quanto quer depositar: '))
        Saldo_Adicionado += depositar
        totdepositado.append(depositar)
        print('Depositado com sucesso')
    if opcao == 3 :
        valor_saque = float(input('Valor do saque: '))
        if valor_saque > limite_saque :
            print('ERRO LIMITE DO SAQUE ULTRAPASSADO ')
        elif valor_saque > Saldo_Adicionado:
            print('VOCÊ NÃO TEM ESSE DINHEIRO')
        else:
            Saldo_Adicionado -= valor_saque
            totsaque.append(valor_saque)
            print('Saque Feito!')
    if opcao == 4 :
        print(f'Saldo inicial {saldo_inicial}')
        for d in totdepositado:
            print(f'Valor depositado é {d}')
        for s in totsaque:
            print(f'Saque de {s}')
        print(f'Saldo Atualizado {Saldo_Adicionado}')
    if opcao == 5:
        break
print('Ate mais')
