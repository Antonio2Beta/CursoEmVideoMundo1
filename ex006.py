from time import sleep
num = int(input('\033[1;31mDigite um número: \033[m'))
print('\033[0;36mAguarde um momento, por favor... \033[m')
sleep(4)
print("\033[1;35mEspera mais um pouco... os cálculos..\033[m \033[1;31marrgh!\033[m \033[1;35mSão "
      "muito \033[4;31mdifíceis\033[m\033[1;35m... ")
sleep(5)
print('\033[1;31mAgora vai... espera...\033[m')
sleep(2)
print('\033[1;32mFOI!!!\033[m')
sleep(0.25)
print('O dobro de \033[1;31m{}\033[m é \033[1;36m{}\033[m'.format(num,2*num))
print('O triplo de \033[1;31m{}\033[m é \033[1;32m{}\033[m'.format(num,3*num))
print('A raíz quadrada de \033[1;31m{}\033[m é \033[4;35m{:.2f}'.format(num,num**0.5))
