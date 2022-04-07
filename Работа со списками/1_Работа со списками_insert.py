# Топ языков
# Условие задачи: Топ языков: Python, Java, JS, SQL
# C++ должен стоять в списке после Java
# Выходные данные:
# Топ языков: Python, Java, C++, JS, SQL

langs = ['Python', 'Java', 'JS', 'SQL']

# ***** Можно заменить этот код на: .insert(2, 'C++') *****

langs.insert(2, 'C++')

# nuw_langs = []
# for i_langs in range(2):
#     nuw_langs.append(langs[i_langs])
# nuw_langs.append('C++')
# for i_langs in range(2, len(langs)):
#     nuw_langs.append(langs[i_langs])


print(langs)
