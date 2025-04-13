pessoas = []

def listar_pessoas():
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
    else:
        for p in pessoas:
            print(f"{p['nome']:<30}{p['idade']:>3} anos")

def cadastrar_pessoa(nome, idade):
    pessoas.append({"nome": nome, "idade": idade})
