import math
ang = float(input('\033[1;31mDigite o valor de um angulo: '))
print('\033[1;34mO SENO de \033[1;31m{} \033[1;34mé {:.2f}\n'
      '\033[1;34mO COSSENO de \033[1;31m{} \033[1;34mé {:.2f}\n'
      '\033[1;34mA TANGENTE de \033[1;31m{} \033[1;34mé {:.2f}'.format(ang, math.sin(math.radians(ang)), ang, math.cos(math.radians(ang)), ang, math.tan(math.radians(ang))))

