# ======= RESUMÃO SOBRE FUNÇÃO EM PYTHON =======

# 1. O que é uma função?
# Uma função é um bloco de código que executa uma tarefa específica.
# Ela pode ser reutilizada várias vezes, evitando repetição de código.

# 2. Como criar uma função?
# Usamos a palavra-chave 'def', seguida do nome da função e parênteses.

def saudacao():
    print("Olá, seja bem-vindo!")

# 3. Como chamar (executar) uma função?
saudacao()  # Isso executa a função e imprime a mensagem.

# 4. Função com parâmetros (valores que a função recebe para usar internamente)
def somar(a, b):
    resultado = a + b
    print("A soma é:", resultado)

somar(3, 5)  # Vai imprimir: A soma é: 8

# 5. Função com retorno (return)
# Usamos 'return' para a função devolver um valor para quem chamou.

def multiplicar(x, y):
    return x * y

resultado = multiplicar(4, 6)
print("O resultado da multiplicação é:", resultado)

# 6. Parâmetro com valor padrão (caso nada seja passado)
def apresentar(nome="Visitante"):
    print("Olá,", nome)

apresentar()         # Saída: Olá, Visitante
apresentar("Maria")  # Saída: Olá, Maria

# 7. Função simples para imprimir uma linha
def lin():
    print("--------------------")

# Chamando a função uma vez
lin()

# Usando a função dentro de um laço (loop)
for l in range(21):
    lin()
    print(l)

# 8. Função que mostra um cabeçalho com texto centralizado
def cabecalho(texto):
    lin()
    print(texto.center(20))  # Centraliza o texto em 20 caracteres
    lin()

cabecalho("Menu Principal")
cabecalho("Opções")

# 9. Vantagens de usar funções:
# - Organiza o código
# - Reutiliza trechos de código
# - Facilita testes e manutenção
# - Ajuda na legibilidade

# =============================================
# DICA: Nome de função deve ser simples e descrever o que ela faz, exemplo: calcular_media(), mostrar_mensagem(), etc.

# ======= FUNÇÕES EXTRAS PARA FACILITAR SEUS CÓDIGOS =======

# 10. Mostrar lista com índice (enumerando itens)
def mostrar_lista_com_indices(lista):
    for i, item in enumerate(lista):
        print(f"{i}: {item}")

# 11. Verifica se valor está em uma lista
def valor_existe(valor, lista):
    return valor in lista

# 12. Criar dicionário de pessoa com dados básicos
def criar_pessoa(nome, idade):
    return {"nome": nome, "idade": idade}

# 13. Mostrar todos os itens de um dicionário com chave e valor
def mostrar_dicionario(d):
    for chave, valor in d.items():
        print(f"{chave}: {valor}")

# 14. Calcular média de uma lista
def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0

# 15. Encontrar maior e menor número de uma lista
def extremos(lista):
    return max(lista), min(lista)

# 16. Repetir uma mensagem várias vezes
def repetir(msg, vezes):
    for i in range(vezes):
        print(f"{i+1} - {msg}")

# 17. Formatador de moeda
def moeda(valor):
    return f"R${valor:.2f}".replace('.', ',')

# 18. Entrada segura de número inteiro
def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("ERRO: Digite um número inteiro válido.")

# 19. Pausa para o usuário apertar Enter
def pausa():
    input("Pressione Enter para continuar...")

# 20. Menu simples com opções
def menu(opcoes):
    cabecalho("MENU DE OPÇÕES")
    for i, item in enumerate(opcoes, start=1):
        print(f"{i} - {item}")
    lin()
    escolha = leia_int("Escolha uma opção: ")
    return escolha

# 21. Contar quantas vezes um valor aparece em uma lista
def contar_ocorrencias(valor, lista):
    return lista.count(valor)

# 22. Verifica se dicionário tem uma chave
def tem_chave(chave, dicionario):
    return chave in dicionario

# 23. Adiciona item ao dicionário se a chave não existir
def adicionar_se_nao_existir(d, chave, valor):
    if chave not in d:
        d[chave] = valor

# 24. Função que cria dicionário com dados inseridos via input
def input_pessoa():
    nome = input("Nome: ")
    idade = leia_int("Idade: ")
    return {"nome": nome, "idade": idade}

# 25. Verifica se número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")

# 26. Apresentar pessoa com nome e idade
def apresentar_pessoa(nome, idade):
    print(f"Olá, {nome}! Você tem {idade} anos.")

# 27. Calcular média de dois números
def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

# 28. Retorna se é maior de idade (booleano)
def maior_de_idade(idade):
    return idade >= 18

# =============================================
