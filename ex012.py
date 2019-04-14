preco = float(input('\033[4;32mDigite o preço do produto: R$'))
valorDesconto = int(input('Digite o valor do desconto(valor inteiro): '))

promocao = valorDesconto/100
desconto = preco - (preco*valorDesconto)
print("\033[1;32mO produto que custava \033[1;31m{}\033[1;32m, com \033[4;36m{}%\033[1;32m de desconto, "
      "passará a custar \033[1;36m{}".format(preco, valorDesconto, preco - (preco * 0.05)))
