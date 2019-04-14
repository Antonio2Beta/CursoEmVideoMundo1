import time
nome = str(input('\033[1;31mDigite seu nome completo: ')).strip()
print('\033[4;35mAnalisando o seu nome, temos que: ')
time.sleep(3)
print('\033[1;31mMaiúsculo: {}'.format(nome.upper()))
print('\033[1;31mMinúsculo: {}'.format(nome.lower()))
print('\033[1;31mSeu nome tem \033[4;34m{}\033[1;31m letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é \033[4;32m{}\033[1;31m e tem \033[4;32m{}\033[1;31m letras'.format(nome.split()[0],len(nome.split()[0])))



