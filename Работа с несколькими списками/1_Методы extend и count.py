print('Пакеты')
# Условие задачи:
# N пакетов по 4 числа (биты: 0 или 1)
# Число -1 означает ошибку
# Если ошибок в пакете <=1, то отправляем в список decode, иначе отбрасываем
# Выводные данные:
# Список decode; кол-во ошибок в списке; кол-во необработанных пакетов.

packet = []
decode = []
bad_packet = 0

# 1) Запрашиваем кол-во пакетов у пользователя
packet_total = int(input('Кол-во пакетов: '))

# 2) цикл for: счетчик // i_packet_num // выводит на экран номер текущего пакета
for i_packet_num in range(packet_total):
    print('\nПакет номер_', i_packet_num + 1)
    # 3) цикл for: счетчик // i_bit // для ввода самого пакета bit состоящего из 4 цифр
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end=' ')
        num = int(input())
        packet.append(num)  # 4) добавит данные в список / packet = [] /
    if packet.count(-1) <= 1: # 5) считает условие при котором аргумент (-1) больше 1 раза
        decode.extend(packet)
    else:
        print('Много ошибок в пакете')
        bad_packet += 1
    packet = []
print('\nПолученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов', bad_packet)
