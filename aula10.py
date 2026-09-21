nome = str(input('\nOlá, qual seu nome? '))
print('\nOlá {}, vamos avaliar a média de suas notas e ver se você passa de ano.\n\nLembrando que a média da escola é 6!'.format(nome))
n1 = float(input('\nDigite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
m = (n1 + n2 + n3)/3

if m >= 6.0:
    print('\nParabéns {}, sua média final é {:.1f} e você passou de ano!'.format(nome, m))
else:
    print('\nEita {}, sua média final é {:.1f} e você vai ter que ficar de recuperação!'.format(nome, m))
