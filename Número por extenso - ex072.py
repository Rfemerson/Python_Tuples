cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onzw', 'doze', 'treze', 'catorze', 'quinze',
        'desseis', 'dessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 < num <= 20:
        print('Tente novamente.', end=' ')
        break
print(f'Você digitou o número {cont[num]}')
