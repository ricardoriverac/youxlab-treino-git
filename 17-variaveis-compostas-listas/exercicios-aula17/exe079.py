valores = []
teste = [1,8,4,0]
testeString = ['Ricardinho','Joao pedro','lucas','jander']
while True:
    numero = int(input('Digite o valor: '))
    if numero in valores:
        print('Valor duplicado.... Não vou adicionar')
        valores.remove(numero)
    valores.append(numero)
    sair = str(input('Quer Continuar [S/N]:')).upper().strip()
    if sair == 'N':
        break
print(sorted(valores))
