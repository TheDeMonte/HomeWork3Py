# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# bin = ""
# number = int(input("10->2: "))
# while number != 0:
#     bin = str(number % 2) + bin
#     number //= 2

# print(bin)


def bin(number):
    if number >= 2:
        bin(number // 2)
    print(number % 2, end='')


bin(int(input("10->2: ")))
