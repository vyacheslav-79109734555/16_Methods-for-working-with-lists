# Сортировка - ВЫБОРОМ
# Напишите программу, которая сортирует элементы списка по
# возрастанию и выводит его на экран.
# Дополнительный список не использовать.
# Пример:
# Изначальный список: [1, 4, -3, 0, 10]

# 2) функция // селекция аргументов //попарно сравнивает аргументы из списка и наименьшее число ставит в начало списка
def selection_arr(my_list):
    # 3) цикл // for i // идет по элементам списка // my_list //
    for i in range(len(my_list)):
        # 4) цикл // for current // производит сравнение текущего элемента списка с минимальным в // my_list //
        for current in range(i, len(my_list)):
            # 5)// if // находит минимальное значение элемента списка
            if int(my_list[current]) < int(my_list[i]):
                # 6)если текущее /current/ элемент меньше элемента / i /
                # меняем их местами в списке элементов // my_list //
                my_list[current], my_list[i] = my_list[i], my_list[current]


print('Введите список натуральных чисел через пробел: ')
n = input()
n = n.split()
# 1) вызов функции // селекция аргументов //
selection_arr(n)
print(n)
