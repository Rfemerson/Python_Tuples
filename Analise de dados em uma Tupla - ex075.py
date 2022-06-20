num1 = int(input('Digite um valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
valores = (num1, num2, num3, num4)
print(f'Você digitou os valores {valores}')
print(f'O número 9 aparece {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 3 apareceu a prmeira vez na posição {valores.index(3)+1}ª')
else:
    print('O valor 3 não foi identificado.')
print('Os valores digitados foram', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')


