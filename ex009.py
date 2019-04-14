from time import sleep
a = int(input('\033[1;34mDigite um número para ver sua tabuada: '))
print(32*"=\033[m")
print('\033[4;31;40mCálculos pesados estão sendo feitos agora...\033[m')
sleep(4)
print("\033[1;36{} x 1  = {} \n{} x 2  = {} \n{} x 3  = {} \n{} x 4  = {} \n{} x 5  = {} \n{} x 6  = {} \n{} x 7  = {} \n{} x 8  = {} \n{} x 9  = {} \n{} x 10 = {}".format(a,a*1,a,a*2,a,a*3,a,a*4,a,a*5,a,a*6,a,a*7,a,a*8,a,a*9,a,a*10))
print(32*"\033[1;34m=\033[m")
