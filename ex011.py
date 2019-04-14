larguraParede = float(input('\033[7;34;37mDigite a largura da parede: \033[m'))
alturaParede = float(input('\033[7;34;37mDigite a altura da parede: \033[m'))
area = alturaParede*larguraParede
tinta = area/2
print('\033[1;30mA parede tem dimensões de \033[1;34m{}x{}\033[1;30m e sua área equivale a \033[1;35m{:.2f}m²'.format(larguraParede,alturaParede,area))
print('\033[1;30mpara pintá-la, você vai precisar de \033[1;36m{:.2f}L de tinta'.format(tinta))
