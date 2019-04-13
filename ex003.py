numero1 = int(input("\033[31mDigite o primeiro número: ")
numero2 = int(input("\033[34mDigite o segundo número: \033[m")
soma = numero1 + numero2
print("A soma entre \033[4;31m{}\033[m e \033[4;34m{}\033[m é \033[4;36m{}\033[m!".format(numero1, numero2, soma))
