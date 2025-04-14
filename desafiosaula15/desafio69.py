usuarioQuerContinuar = ''
pessoasComMaisDe18 = 0
quantosHomens = 0
mulheresComMenosDe20 = 0

while True:
    nome = input('Qual seu {}NOME{}?: '.format('\033[36m', '\033[m'))
    idade = int(input('Qual sua {}IDADE{}?: '.format('\033[35m', '\033[m')))
    sexo = input('Qual seu {}SEXO{}?{}[F/M]{} '.format('\033[34m', '\033[m', '\033[33m', '\033[m')).upper()
    if idade>=18:
        pessoasComMaisDe18+=1
    if sexo == 'M':
        quantosHomens+=1
    if sexo == 'F' and idade<20:
        mulheresComMenosDe20+=1
    usuarioQuerContinuar = input('Você deseja continuar? {}[S/N]{}'.format('\033[33m', '\033[m') ).upper()
    if usuarioQuerContinuar=='N':
        print('PROGRAMA FINALIZADO, VOLTE SEMPRE! ')
        break
        
print('Tem {} pessoas com {}MAIS DE 18 ANOS{}'.format(pessoasComMaisDe18, '\033[35m', '\033[m' ))
print('Tem {} {}HOMENS{} '.format(quantosHomens, '\033[35m', '\033[m'))
print('Tem {} {}MULHERES com MENOS DE 20 ANOS{} '.format(mulheresComMenosDe20, '\033[35m', '\033[m'))
