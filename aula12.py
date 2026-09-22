nome = str(input('\nDigite seu nome: ')).title().strip()

if nome == 'Vinicius':
    print('\nQue nome bonito!')

elif nome in 'Pedro João Joao Mateus Matheus':
    print('\nSeu nome é comum no Brasil!'.format(nome))

else:
    print('\nSeu nome é feio!'.format(nome))

print('\nTenha um bom dia, {}!'.format(nome))
