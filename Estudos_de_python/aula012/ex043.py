alt=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
IMC= peso/alt**2

if IMC <=18.4:
    print('Você está tripa seca ')
elif IMC >=18.5:
    print('Você está asterisk ')
elif IMC <=29.9: 
    print('Toguro ')
elif IMC <= 34.9:
    print('Pré Thais Carla ')
elif IMC <= 39.9:
    print('Mau Mau')
else:
    print('Thais Carla') 
