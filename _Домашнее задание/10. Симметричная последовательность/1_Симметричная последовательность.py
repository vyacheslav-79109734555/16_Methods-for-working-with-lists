def is_palindrome(num_list):
    reverse_list = []
    for i_n in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_n])
    if num_list == reverse_list:
        return True
    else:
        return False


num = [1, 2, 3, 4, 5]
new_num = []
answer = []

for i_num in range(0, len(num)):
    for j_arr in range(i_num, len(num)):
        new_num.append(num[j_arr])
    if is_palindrome(new_num):
        for i_answer in range(0, i_num):
            answer.append(num[i_answer])
        answer.reverse()
        break
    new_num = []
print('Исходный список:', num)
print('Нужно чисел для палиндрома:', len(answer))
print('Список чисел:', answer)
