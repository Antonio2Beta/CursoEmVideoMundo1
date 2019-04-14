k = int(input('\033[1;34mQual é a velocidade atual do seu veículo? ^^ '))
if k <=80:
    print('\033[1;36mDirija com segurança, cidadão!')
    print('\033[4;32mTenha um bom dia! ^^')
else:
    multa = 7*(k-80)
    print('\033[1;31mMULTADO! >=) \n'
          'Você vai pagar uma multa de \033[4;30m{}\033[1;31m reais'.format(multa))

