from time import sleep
numero = int(input('\033[34mDigite um número: '))
print('\033[4;31mAguarde enquanto os dados são processados...\033[m')
sleep(2)
print("Analisando o número \033[4;32m{}\033[m, seu antecessor é \033[1;31m{}\033[m "
      "e seu sucessor é \033[1;36m{}".format(numero, numero - 1, numero + 1))
