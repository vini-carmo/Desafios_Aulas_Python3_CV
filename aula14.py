n = 1                                   # Variável "n" iniciada com o valor 1
par = impar = 0                         # Variáveis "par" e "ímpar" iniciadas com o valor 0
while n != 0:                           # Enquanto (while) "n" for diferente (!=) de 0, o programa vai continuar pedindo valor para o usuário
    n = int(input('Digite um valor: '))
    if n != 0:                          # Aqui é para o programa não contabilizar "0" como número par
        if n % 2 == 0:                  # Aqui verifica se o número é par, e se for, a variável "par" recebe quantos números pares foram digitados
            par += 1
        else:                           # Aqui verifica se o número é ímpar, e se for, a variável "impar" recebe quantos números ímpares foram digitados
            impar += 1
print('\nVocê digitou {} números pares e {} números ímpares!'.format(par, impar))
