n = int(input('Кол-во друзей: '))  # Кол-во друзей: 3
k = int(input('Долговых расписок: '))  # Долговых расписок: 1
debts_list = []

for i in range(1, n + 1):
    debts_list.append(list([i, 0]))
print(debts_list)

for i in range(k):
    print('\n', i + 1, 'расписка:')
    a = int(input('Кому: '))  # Кому: 3
    b = int(input('От кого: '))  # От кого: 1
    c = int(input('Сколько: '))  # Сколько: 100
    if a != b:
        debts_list[a - 1][1] -= c
        debts_list[b - 1][1] += c
    else:
        print('Гарантируется, что ни один друг не брал в долг сам у себя.')
        break
print('\nБаланс друзей:')
for i in range(len(debts_list)):
    print(debts_list[i][0], ':', debts_list[i][1])
