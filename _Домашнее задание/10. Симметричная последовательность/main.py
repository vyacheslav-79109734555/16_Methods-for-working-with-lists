x = int(input('Кол-во чисел: '))
n_list = []
for _ in range(x):
    print('Число: ', end='')
    n = int(input())
    n_list.append(n)
print('\nПоследовательность: ', n_list)
i = 0
while n_list != n_list[::-1]:
    n_list.insert(x, n_list[i])
    i += 1

print('Нужно приписать чисел:', i)
print('Сами числа: ', n_list[:i][::-1])
print('Палиндром : ', n_list)
