produto = float(input('Qual o valor do produto? R$'))
avista = produto - (produto * 10 / 100)
parcelado = produto + (produto * 10 / 100)
parcelas = parcelado / 12
print('O valor do produto à vista com desconto de 10% sai por R${:.2f}.\nSe for parcelado, o valor total do produto sai por {:.2f}!'.format(avista, parcelado))
print('As parcelas podem ser em até 12x de R${:.2f}!'.format(parcelas))
