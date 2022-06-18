times = ('Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR',
         'São Paulo', 'Atlético-MG', 'Avaí', 'Santos', 'Bragantino',
         'Flamengo', 'Fluminense', 'Coritiba', 'América-MG', 'Botafogo',
         'Ceará', 'Goiás', 'Atlético-GO', 'Cuiabá', 'Juventude', 'Fortaleza')
print('=*' * 30)
print('TABELA BRASILEIRÃO 2022')
print('=*' * 30)
print('Classificados para a Libertadores 2023')
print(times[:5])
print('=*' * 30)
print('Rebaixados para a Serie B')
print(times[15:])
print('=*' * 30)
print('Times que disputaram o campeonato')
print(sorted(times))
print('=*' * 30)
print(f'O Ceará está na {times.index("Ceará")+1}ª posição')
