from time import sleep
real = float(input('\033[4;34mDigite uma quantia em reais: R$\033[m'))
print('\033[7;31;40mCalculando cota atual do dólar...\033[m')
sleep(3)
dolar = real / 3.27
print("\033[1;30mCom \033[1;34m{:.2f} reais, \033[1;30mdá pra "
      "comprar \033[1;32m{:.2f} dólares".format(real, dolar))
