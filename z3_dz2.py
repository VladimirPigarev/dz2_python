# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input("Введите число "))
list_numbers = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Последовательность: {list_numbers}\nСумма: {round(sum(list_numbers), 2)}')