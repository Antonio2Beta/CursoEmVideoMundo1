import random,time
aluno1 = str(input('\033[1;36mPrimeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: \033[m'))
lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print('\033[4;31mSORTEANDO ORDEM DE APRESENTAÇÃO...\033[4;34m')
time.sleep(5)

print(lista)

