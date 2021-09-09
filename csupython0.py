#Найти максимальный элемент в списке чисел
numbers = [1, 2, 30, 25, 60, 999, 1488]
cur_max = 0

for x in numbers:
    if x > cur_max:
        cur_max = x

print(cur_max)