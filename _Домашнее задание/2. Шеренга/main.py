a = list(range(160, 178, 2))
b = list(range(162, 183, 3))

c = sorted(a + b)

print('Отсортированный список учеников:', list(set(c)))
