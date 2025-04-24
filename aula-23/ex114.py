import webbrowser
try:
    webbrowser.open('https://www.pudim.com.br/')
    print('O site pudim está acessível')
except:
    print('O site não está acessível')