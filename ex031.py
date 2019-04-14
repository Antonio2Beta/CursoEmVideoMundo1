from time import sleep
distancia = float(input('\033[1;36mQual é a distância da viagem em Km? '))
preco = distancia*0.5 if distancia<=200 else distancia*0.45
print('Calculando valor da passagem')
sleep(5)
print('\033[1;32mSua passagem vai custar  \033[4;35mR${:.2f} reais'.format(p))
