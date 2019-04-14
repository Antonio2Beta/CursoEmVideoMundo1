from datetime import date
ano = int(input('\033[1;35mDigite um ano. Digitar \033[1;34mzero \033[1;35mirá considerar o ano \033[1;34matual '))
if ano == 0:
    ano = date.today().year
print('\033[4;31m{}\033[1;35m é Bissexto'.format(ano) if ano%4==0 and ano%100!=0 or ano%400==0 else '\033[4;31m{}\033[1;35m não é bissexto'.format(ano))
