while True:
    nome = str(input('\033[4;33mDigite seu nome completo: ')).title().strip()
    print('\033[1;36mExiste Silva no seu nome?', 'Silva' in nome)
