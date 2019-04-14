import time
frase = str(input('\033[1;35mDigite uma frase: ')).upper().strip().replace('Á','A')
print('\033[7;35;37mPROCESSANDO DADOS...\033[m')
time.sleep(3)
print('\033[1;32mA letra A aparece \033[1;31m{}\033[1;32m vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição \033[1;31m{}'.format(frase.find('A')+1))
print('\033[1;32mA última letra A aparece na posição \033[1;31m{}'.format(frase.find('A',-1)+1))
