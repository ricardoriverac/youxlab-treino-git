from colorama import init, Fore, Back, Style
import time

# Inicializa o colorama
init(autoreset=True)

def mostrar_titulo(msg, cor=Fore.WHITE):
    print(Back.BLUE + cor + '=' * (len(msg) + 4))
    print(Back.BLUE + cor + f'  {msg}  ')
    print(Back.BLUE + cor + '=' * (len(msg) + 4))

def sistema_ajuda():
    while True:
        mostrar_titulo('SISTEMA DE AJUDA PyHELP', Fore.YELLOW)
        comando = input(Fore.GREEN + 'Função ou biblioteca > ').strip()
        if comando.upper() == 'FIM':
            mostrar_titulo('ATÉ LOGO!', Fore.RED)
            break
        else:
            mostrar_titulo(f"Acessando o manual do comando '{comando}'...", Fore.CYAN)
            time.sleep(1)
            print(Fore.WHITE)
            help(comando)

sistema_ajuda()