from colorama import init, Fore, Back, Style
import time
init(autoreset=True)

def mostrar_titulo(msg, cor=Fore.WHITE):
    print('=-' * (len(msg) + 4))
    print( f'  {msg}  ')
    print('=-' * (len(msg) + 4))

def sistema_ajuda():
    while True:
        mostrar_titulo('Sistema de ajuda PyHELP', Fore.YELLOW)
        comando = input(Fore.GREEN + 'Função ou biblioteca > ').strip()
        if comando.upper() == 'FIM':
            mostrar_titulo('ATÉ LOGO!', Fore.RED)
            break
        else:
            mostrar_titulo(f"Olhando o manual do comando '{comando}'...", Fore.CYAN)
            time.sleep(1)
            print(Fore.WHITE)
            help(comando)

sistema_ajuda()