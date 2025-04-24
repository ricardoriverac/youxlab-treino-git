imovel = float(input('Qual o valor do imovel: '))
renda = float(input('Qual o sua renda: '))
parcela = float(input('Em quantos anos vai parcelar: '))
valorAnual = (imovel/parcela)/12

mensalidade = renda*30/100
if mensalidade >= valorAnual:
    print (f'Seu imprestimo foi aprovado, suas parcelas serao {valorAnual}') 
else: 
    print (f'Seu imprestimo foi recusado o valor da parcela mensal é R${valorAnual} ultrapassou 30% de sua renda mensal R${renda}')
