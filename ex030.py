print('\033[1;32mDigite um número aí que eu vou dizer se é ou não par: ')
x = int(input())
print('\033[1;32mÉ \033[1;34mpar \033[1;32messe número' if x%2 == 0 else '\033[1;32mEsse número é \033[1;34mímpar')
