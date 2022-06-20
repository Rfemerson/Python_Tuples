precos = ('Hamburguer', 25, 'Batata frita', 10, 'Coca-cola, 360ml', 5, 'Milk Shake', 18,)
print('=' * 40)
print(f'{"Cardápio EFR BURGUER":^40}')
print('=' * 40)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print(f'{precos[pos]:.<30}', end=' ')
    else:
        print(f'R${precos[pos]:>5}')
