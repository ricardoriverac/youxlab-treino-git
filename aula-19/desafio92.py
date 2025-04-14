from datetime import date
dados = {}
dados["Nome"] = str(input("Nome do cidadão: ")).strip().title()
AnoNasc = int(input("Ano de Nascimento: "))
AnoAtual = date.today().year
dados["Idade"] = AnoAtual - AnoNasc 
dados["Carteira"] = int(input("Número da carteira de trabalho (0 caso não tenha): "))
if dados["Carteira"] != 0:
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário do funcionário:R$ "))
    AnoAposentadoria = dados["Ano de contratação"] + 35
    IdadeAposentadoria = AnoAposentadoria - AnoNasc
    dados["Aposentadoria"] = IdadeAposentadoria
    print("="*55)
    print(f'''    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: {dados["Carteira"]}
    - Ano de contratação: {dados["Ano de contratação"]}
    - Salário: R${dados["Salário"]}
    - Idade da aposentadoria: {dados["Aposentadoria"]}''')
else:
    print("="*50)
    print(f'''    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: Não possui, o cidadão está desempregado''')
