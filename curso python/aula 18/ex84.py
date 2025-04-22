pessoas = list()
dados = list()
continuacao = "S"
while continuacao == "S":
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    continuacao = str (input ("Quer continuar [S/N] ? ")).strip().upper()
print (f"Quantas pessoas foram cadastradas {len(pessoas)}")
print (pessoas)
pesoPesado = 0
count = 0
pesoLeve = 0
maisPesados = list()
maisLeves = list()
for p in pessoas:
    if p[1] > pesoPesado and count != 0:
        print(f'{p[1]} if')
        pesoPesado = p[1]
        maisPesados = [p[0]]
    elif p[1] == pesoPesado and count != 0:
        print(f'{p[1]} elif')
        pesoPesado = p[1]
        maisPesados.append(p[0])
    else:
        print(f'{p[1]} else')
        pesoLeve = p[1]
        maisLeves = [p[0]]
    count+=1
        
print (f"{maisLeves} tem o peso igual há: {pesoLeve} e é o menor de peso!!!")    
print (f"{maisPesados} tem o peso igual há: {pesoPesado} e é o maior de peso!!!")    