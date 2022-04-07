n = int(input('Кол-во человек: '))  # Кол-во человек: 5
n_list = list(range(1, n + 1))
k = int(input('Какое число в считалке?  '))  # Какое число в считалке? 7
print('Значит, выбывает каждый', k, 'человек')
stop = 0

for i in range(n - 1):
    print('\nТекущий круг людей: ', n_list)
    start = stop % len(n_list)
    print('Начало счёта с номера', n_list[start])
    stop = (start + k - 1) % len(n_list)
    print('Выбывает человек под номером', n_list[stop])
    n_list.remove(n_list[stop])
print('\nОстался человек под номером', n_list[stop])


