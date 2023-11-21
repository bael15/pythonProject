# print('Добро пожаловать на викторину:')
#
# asks = {
#     'назовите самый большой остров в мире.': 'Гренландия',
#     'в какой стране производится больше всего кофе в мире?': 'Бразилия',
#     'какая самая яркая звезда на небе?': 'Сириус',
#     'из какого ореха делают марципан?': 'Миндаль'
# }
#
# score = 0
#
#
#
#
#
#
# for i, j in asks.items():
#     print(i)
#     answer = str(input("ваш ответ: "))
#     if answer == j:
#         print('правильный ответ!')
#         score += 1
#     else:
#         print("ответ не верный")
#
# print('вы набрали %s очка' %score)
#
#
#
#
#
#
# contacts = []
#
# while True:
#     contact = {}
#     print("Введите информацию о контакте (для выхода введите 'q'):")
#     contact['Имя'] = input("Имя: ")
#     if contact['Имя'] == 'q':
#         break
#
#     contact['Фамилия'] = input("Фамилия: ")
#     contact['День рождения'] = input("День рождения: ")
#     contact['Номер телефона'] = input("Номер телефона: ")
#
#     contacts.append(contact)
#
#
#




# a = input("Введи что то: ")
#
# vowels = "aeiouAEIOU"
#
# for char in a:
#     if char in vowels:
#         continue
#     else:
#         print(char)
#
#
#
#
#
#
# def f(**kwargs):
#     print(kwargs)
# f(a=1, b=5, c=6)


#
#
# def f(*args):
#     print(args)
# f(1,2,3,4,5,6,7)

# try:
#     num1 = float(input("ВВедите превое число"))
#     num2 = float(input("Введите второе число"))
#     result = num1 / num2
#     print("результат деления:", result)
# except ZeriDivisionError:
#     print("ошибка: деления на ноль")





# while True:
#     user_input = input("введи строку:")
#     try:
#         number = int(user_input)
#         print("Число:", number)
#         break
#     except ValueError:
#         print("Это не число. Попробуйте снова.")


def remove_duplicates(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list



my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = remove_duplicates(my_list)
print(f"Список без повторяющихся чисел: {unique_list}")
def find_average(lst):
    average = sum(lst) / len(lst)
    return average
average_result = find_average(my_list)
print(f"Среднее значение списка: {average_result}")