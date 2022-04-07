list_1 = []
list_2 = []

for i in range(3):
    print('Введите', i + 1, ' число для первого списка: ', end='')
    n = int(input())
    list_1.append(n)

for i in range(7):
    print('Введите', i + 1, ' число для второго списка: ', end='')
    n = int(input())
    list_2.append(n)

print('\nПервый список:', list_1)
print('Второй список:', list_2)
c = list_1 + list_2
print('\nНовый первый список с уникальными элементами:', list(set(c)))

