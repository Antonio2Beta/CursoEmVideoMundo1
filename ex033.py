x = float(input('\033[1;31mDigite o 1º nº: '))
y = float(input('\033[1;32mDigite o 2º nº: '))
z = float(input('\033[1;34mDigite o 3º nº: '))
#maior = max(x,y,z)
#menor = min(x,y,z)
maior = x
if (y>x) and (y>z):
    maior=y
if (z>x) and (z>y):
    maior=z
menor = x
if (y<x) and (y<z):
    menor=y
if (z<y) and (z<x):
    menor=z
print("\033[1;35mO maior número é o \033[4;30m{}\n"
      "\033[1;35mO menor número é o \033[4;30m{}".format(maior, menor))
