from datetime import datetime
anoAtual = datetime.now().year
pessoa = {}
pessoa ['nome'] = input('nome: ' )
nascimento = int (input('ano de nascimento: '))
pessoa['idade'] = anoAtual - nascimento
pessoa['ctps'] = int (input('número da ctps, (digite 0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['anoContratacao'] = int (input('ano de contratação: ' ))
    pessoa['salário'] = float (input('salário: R$ ' ))
    anosTrabalhados = anoAtual - pessoa['anoContratacao']
    anosFaltando = 35 - anosTrabalhados
    if anosFaltando < 0:
        anosFaltando = 0
    idadeAposentadoria = pessoa['idade'] + anosFaltando
    pessoa['aposentadoria'] = f"{idadeAposentadoria} anos"
print ('-=' * 4, f'\033[35m DADOS CADASTRADOS!! \033[m','-=' * 4 )
for chave in pessoa:
    print (chave, ':', pessoa[chave])