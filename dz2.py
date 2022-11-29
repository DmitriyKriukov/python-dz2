# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# num = input('Введите число: ')
# sum = 0
# for el in num:
#     if el != '.':
#         sum += int(el)
# print(f'сумма цифр {num} равна {sum}')


# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# n = int(input('Введите число: '))
# some_list = []
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
#     some_list.append(fact)
# print(some_list)


# 16. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# some_dirt = {}
# n = int(input('Введите число: '))
# sum = 0
# for i in range(1, n + 1):
#     some_dirt[i] = round((1 + 1 / i) ** i, 2)
#     sum += some_dirt[i]
# print(some_dirt)
# print(sum)



# 18. Реализуйте алгоритм перемешивания списка.
# import random
# some_list = [1, 2, 3, 4, 5]
# random.shuffle(some_list)
# print(some_list)