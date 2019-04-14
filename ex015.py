kilometer = float(input('Quantos quilômetros você rodou com esse caro?: '))
days = int(input('Há quantos dias você o alugou?'))
preco = (60*days) + (0.15*kilometer)
print('Você precisará pagar R${:.2f}'.format(preco))


