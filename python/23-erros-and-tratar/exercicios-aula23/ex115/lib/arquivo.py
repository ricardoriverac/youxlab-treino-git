from lib import interface

def arquivoexiste(nome):
    try:
        abrir =  open(nome , 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criaraarquivo(nome):
    try:
        abrir = open(nome , 'wt+')
        abrir.close()
    except:
        print('Houve um problema ')
    else:
        print(f'O arquivo {nome} criado com sucesso')
def lerarquivo(nome):
    try:
        a = open(nome , 'rt')
    except:
        print('Não consegui ler o arquivo')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} idade')
    finally:
        a.close()
def novocadastro(arq , nome='desconhecido' , idade=0):
    try:
        a = open(arq , 'at')
    except:
        print('Houve um problema no cadastro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um problema a cadastrar a pessoa')
        else:
            print(f'Cadastrato com sucesso a pessoa {nome}')
            a.close()