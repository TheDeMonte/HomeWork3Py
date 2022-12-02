# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21}

def Fib(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
# def negativeFib(n):
    

k = int(input('Число: '))
data = list(Fib(k))
print(data)

