violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input('Сколько песен выбрать? '))
sound_time = 0
for i in range(n):
    print('Название', i + 1, 'песни: ', end='')
    text = input()
    for arr in violator_songs:
        if arr[0] == text:
            sound_time += arr[1]
print('Общее время звучания песен:', round(sound_time, 2))
