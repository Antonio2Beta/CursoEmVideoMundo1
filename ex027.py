nome = str(input('\033[1;36mDigite seu nome completo: ')).strip().title()
n = nome.split()
print('\033[1;34mMuito prazer em conhecê-lo(a), \033[4;31m{}!'.format(nome))
print('\033[1;34mSeu primeiro nome é \033[4;31m{}'.format(n[0]))
#print('Seu último nome é {}'.format(n[-1]))
print('\033[1;34mSeu último nome é \033[4;31m{}'.format(n[len(n)-1]))
