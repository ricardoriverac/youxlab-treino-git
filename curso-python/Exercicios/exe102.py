# Crie um programa que tenha uma função fatoriaç() que recebe dois parametros: o primeiro que indique o número
# A calcular e o outro chamado show, que será um valor logico (opcional) indicando se será mostrado ou não
# na tela o processo de calculo fatorial.

def quebraLin():
    print("\n")

def cabecalho(texto):
    largura = len(texto) + 8
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

def fatorial(n=1, show=False):
    """
    Calcula o fatorial de um número com opção de mostrar o processo.
    :param n: Número para calcular o fatorial
    :param show: (opcional) Mostrar ou não o processo de cálculo
    :return: Resultado do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f"{c}", end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f

num = int(input("Digite um número para calcular o fatorial: "))
mostrar = input("Deseja ver o processo (s/n)? ").strip().upper() == 'S'

quebraLin()
cabecalho("Processo:" if mostrar else "Resultado:")
quebraLin()

print(fatorial(num, show=mostrar))
