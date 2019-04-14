import time
num = int(input('\033[1;34mDigite um número: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('\033[4;35mAnalisando o número informado: ')
time.sleep(2)
print('\033[1;32mUnidade: {}'.format(u))
print('\033[1;32mDezena:  {}'.format(d))
print('\033[1;32mCentena: {}'.format(c))
print('\033[1;32mMilhar:  {}'.format(m))

