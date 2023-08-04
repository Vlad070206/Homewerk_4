"""Найдите сумму цифр трехзначного числа."""

# Вариант 1 
n = 123
n1 = n // 100  # Нахождение первой цифры числа
n2 = (n % 100) // 10  # Нахождение второй цифры числа
n3 = n % 10  # Нахождение третьей цифры числа

print(n1 + n2 + n3)


# Вариант 2
n = 123
n = str(n)
print(int(n[0]) + int(n[1]) + int(n[2]))


# Вариант 3
n = 123
number_sum = 0
for number in str(n):
    number_sum += int(number)


# Вариант 4
n = 123
print(sum(int(i) for i in str(n)))
"""Генератор (цикл) внутри вернёт список
[int(i) for i in input("Введиет число: ")] -> [1, 2, 3]
sum([1, 2, 3]) -> 6 получаем сумму элементов"""


# Вариант 5 - Забегая вперёд
n = 123
print(sum(map(int, str(n))))