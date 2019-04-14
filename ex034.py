from time import sleep
sal = float(input('\033[1;31mQuanto você ganha? '))
reajuste = sal*1.15 if sal<=1250 else sal*1.10
print('Calculando o seu reajuste...')
sleep(3)
print('\033[1;36mCom o reajuste, seu salário será de \033[4;32mR${} reais'.format(reajuste))
