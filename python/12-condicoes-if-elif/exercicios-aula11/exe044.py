produto = float(input('Qual é o preço do produto: R$'))
print("""FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão      
[3] 2x no cartão      
[4] 3x ou mais no cartão """)
opcao = int(input('Digite a opção: '))
if opcao == 1 :
    vp = produto + (produto * 5/100)
    print(f'O produto que custuvá {produto} custará {vp}')
elif  opcao == 2 : 
    vp = produto + (produto * 10/100)
    print(f'O produto que custuvá {produto} custará {vp}')
elif opcao == 3 :
    divisao = produto/2
    print(f'Você parcelou em 2x e pagará {divisao}')
    print(f'O produto que custuva {produto} custará {produto}')  
elif opcao == 4 :
    parcela = int(input('Quantas parcelas você quer:'))
    vp = produto + (produto * 20/100)
    juros = vp/parcela 
    print(f'Você parcelou em {parcela}x é pagara {juros:.2f} com JUROS')
    print(f'O produto que antes custuvá {produto} agora com 20% de juros custará {vp}')