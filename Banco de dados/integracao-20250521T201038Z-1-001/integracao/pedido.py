import psycopg2

conexao = psycopg2.connect(database = "pedido",
                           host = "localhost",
                           user = "postgres",
                           password = "123456",
                           port = "5432")
#print(conexao.info)
#print(conexao.status)

cursor = conexao.cursor()
#cursor.execute('select * from cliente')
#print(cursor.fetchall())

#cursor.execute('select * from dados_pedido')
#print(cursor.fetchall())

#cursor.execute('select * from cliente_dados')
#print(cursor.fetchall())

#novo_bairro = input('Digite o nome do novo bairro: ')
#print(novo_bairro)
#cursor.execute("insert into bairro (nome) values ('{nome}')".format(nome = novo_bairro))
#conexao.commit()

#novo_bairro = input('Digite o novo nome do bairro: ')
#idbairro = int(input('Digite o id do bairro a ser alterado: '))
#print(novo_bairro, idbairro)
#cursor.execute("update bairro set nome = '{nome}' where idbairro = {id}".format(nome = novo_bairro, id = idbairro))
#conexao.commit()

#idbairro = int(input('Digite o id do bairro a ser apagado: '))
#cursor.execute("delete from bairro where idbairro = {id}".format(id = idbairro))
#conexao.commit()

#idcliente = int(input('Digite o id para obter o nome: '))
#cursor.execute("select get_nome_by_id({id})".format(id = idcliente))
#print(cursor.fetchall())

#cursor.execute("select formata_moeda(valor) from pedido")
#print(cursor.fetchall())

#cursor.execute("call reajusta_produto(3, 10)")
#conexao.commit()

cursor.execute('select cln.nome as cliente,	sum(pdd.valor) as total from pedido pdd left outer join cliente cln on pdd.idcliente = cln.idcliente group by cln.nome')
dados = cursor.fetchall()
#print(dados)

colunas = []
for col in cursor.description:
    #print(col[0])
    colunas.append(col[0])
#print(colunas)

import pandas as pd
df = pd.DataFrame(data = dados, columns=colunas)
print(df)

import matplotlib.pyplot as plt
plt.barh(df['cliente'], df['total'])
plt.show()

plt.pie(df['total'], labels=df['cliente'])
plt.show()














