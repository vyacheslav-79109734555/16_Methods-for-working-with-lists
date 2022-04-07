guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def greeting():
    name = input('Имя гостя: ')
    if len(guests) < 6:
        print('Привет!', name)
        guests.append(name)
    else:
        print('Прости,', name, 'но мест нет.')


while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    text = input('Гость пришел или ушел?  ')
    if text != 'Пора спать' and text == 'пришел':
        greeting()
    elif text == 'ушел':
        name = input('Имя гостя: ')
        print('Пока!', name)
        guests.remove(name)
    else:
        print('\nВечеринка закончилась, все легли спать.')
        break
