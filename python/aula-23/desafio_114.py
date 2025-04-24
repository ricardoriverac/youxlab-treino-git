import requests
try:
    site = input('https://images.app.goo.gl/7LUfyrrnbUKcVMVYA: ')
    check = requests.get(site)
    print('Site está acessível.')
except:
    print(f'Site está indisponível.')