from math import hypot
from time import sleep
catetoOposto = float(input('\033[1;35mDigite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
print('\033[4;31mPROCESSANDO CÁLCULO DA HIPOTENUSA')
sleep(3)
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print('\033[1;34mA \033[4;31mhipotenusa \033[1;34mé \033[1;31m{:.2f}'.format(hipotenusa))
