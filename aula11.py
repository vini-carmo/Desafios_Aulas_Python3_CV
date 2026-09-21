cor = str(input('\nMe diga a cor da letra desejada entre Vermelho, Verde, Amarelo, Azul, Roxo, Ciano e Cinza: ')).title().strip()

if cor == 'Vermelho':
    cor = '\33[31mVermelho\33[m'

if cor == 'Verde':
    cor = '\33[32mVerde\33[m'

if cor == 'Amarelo':
    cor = '\33[33mAmarelo\33[m'

if cor == 'Azul':
    cor = '\33[34mAzul\33[m'

if cor == 'Roxo':
    cor = '\33[35mRoxo\33[m'

if cor == 'Ciano':
    cor = '\33[36mCiano\33[m'

if cor == 'Cinza':
    cor = '\33[37mCinza\33[m'

print('\nA cor da letra desejada é {}'.format(cor))
