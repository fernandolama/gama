usuario = input('Insira o seu nome de usuário: ')
senha = input('Insira sua senha: ')

while usuario == senha:
    print('Seu usuário e sua senha são iguais. Insira um nome de usuário e senha diferentes.')
    usuario = input('Insira o seu nome de usuário: ')
    senha = input('Insira sua senha: ')

print('Informações cadastradas com sucesso! Fim do programa.')