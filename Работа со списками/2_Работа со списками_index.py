# Топ языков
# Условие задачи: Топ языков: Python, Java, JS, SQL
# C++ должен стоять в списке после Java


langs = ['Python', 'Java', 'JS', 'SQL']
print(langs)

user_langs = input('После чего вставить: ')
i_langs = langs.index(user_langs)
langs.insert(i_langs + 1, 'C++')

print(langs)
