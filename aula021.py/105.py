def notas(*numero,situacao=False):

    dados = {}

    dados['total'] = len(numero)
    dados['Menor'] = max(numero)
    dados ['Maior'] = min(numero)
    dados ['media'] = sum(numero)/len(numero)

    if situacao: 

        if dados['media'] <=  6:
            dados['media'] 
            

        elif dados ['media'] >=7 and <= 9:
            


    return dados





#esposta = notas

















