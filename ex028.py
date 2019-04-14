import random
import time

print(40*'\033[1;31m-=-')
print('\033[4;36mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print(40*'\033[1;31m-=-')
x = random.randrange(0,5)
print('\033[1;30;36mEstou pensando ... ')
time.sleep(5)
num = int(input('\033[4;35mAdivinhe o número: '))
if num<0 or num >5:
    print('\033[4;31mAnimal! Eu disse: entre 0 e 5!!!')
else:
    print('\033[1;32mAcertou mizerávi!' if num == x else '\033[4;31mErrooou!')
    print('\033[4;35mO número foi {}'.format(x))
