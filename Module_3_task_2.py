import random

def get_numbers_ticket(min, max, quantity):

    return sorted(random.sample(range(min, max+1), quantity))


min_value = int(input("Введите минимальное значение (>1): "))
max_value = int(input("Введите максимальное значение (<1000): "))
quantity = int(input("Введите количество чисел в билете: "))


ticket = get_numbers_ticket(min_value, max_value, quantity)
print("Ваш выигрышный билет:", ticket)