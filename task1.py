"""
Массив чисел Фиббоначи
"""

n = 10
a = 0
b = 1
f = [a]

for i in range(n):
    temp = a
    a = b
    b += temp
    f.append(a)

print('Fibbinacci nubmer for {} is {}'.format(n, a))