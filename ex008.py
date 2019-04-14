from time import sleep
numero = float(input('\033[1;32mDigite um valor em metros: '))
print('\033[4;32mAnalisando o número digitado...\033[m')
sleep(2)
print('\033[4;32mFazendo cálculos precisos aqui. Por favor, aguarde...\033[m')
sleep(5)
print("{}m \033[1;35mequivalem a \033[1;36m\n{}km, \n{}hm, \n{}dam, \n{}dm, \n{}cm \033[1;35m\n"
      "ou \033[1;36m{}mm".format(numero, numero / 1000, numero / 100, numero / 10, numero * 10, numero * 100, numero * 1000))

