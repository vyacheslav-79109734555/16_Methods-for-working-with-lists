n_list = []
k_list = []
rental = []
x = int(input('Кол-во коньков: '))
for i in range(x):
    print('Размер', i + 1, 'пары: ', end='')
    a = int(input())
    n_list.append(a)

y = int(input('Кол-во людей: '))
for i in range(y):
    print('Размер', i + 1, 'пары: ', end='')
    b = int(input())
    k_list.append(b)

for i in range(len(n_list)):
    for w in range(len(k_list)):
        if n_list[i] == k_list[w]:
            rental.append(n_list[i])
            n_list[i] = n_list[i] - k_list[w]

print('Наибольшее кол-во людей, которые могут взять ролики: ', len(rental))

# ************** или как вариант может через: // .count() //*******************************

n_1_list = [41, 40, 39, 42]
k_1_list = [42, 41, 42]
x = 0

for i in range(len(n_1_list)):
    for w in range(len(k_1_list)):
        if n_1_list[i] == k_1_list[w]:
            x = n_1_list.count(int(n_1_list[i]))
            x += x

print('\nПрокат, ролики в наличии:', n_1_list)
print('Желающие покататься_размер:', k_1_list)
print('Наибольшее кол-во людей, которые могут взять ролики: ', x)
