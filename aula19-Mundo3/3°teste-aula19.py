dados={'nome':'João', 'sexo':'M', 'idade':28}

del dados['sexo']  #DELETOU o item sexo

dados['nome']='Lucas'  #TROCOU o nome João por Lucas 

dados['peso']=70   #ADICIONOU um item na lista

for chave, valor in dados.items():   
    print(f'{chave} = { valor}')