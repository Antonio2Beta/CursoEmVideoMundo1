from time import sleep

x = float(input('\033[1;36mMedida da primeira reta: '))
y = float(input('\033[1;35mMedida da segunda reta: '))
z = float(input('\033[1;34mMedida da terceira reta: '))
print('\033[32mVerificando se as 3 retas podem ou não formar um triângulo...\nIsso pode levar alguns segundos...')
sleep(4)
print('\033[1;32mAs retas formam um triângulo' if abs(x-y)<z<x+y and abs(z-x)<y<z+x and abs(z-y)<x<z+y else '\033[1;31mNão forma triângulo')
