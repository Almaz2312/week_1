# 1. Вывести на экран все числа начиная с 0, пока сумма всех этих чисел не превысит 1000.

i = 0
total = []
while sum(total) <= 1000:
    total.append(i)
    print(i)
    i += 1


# 2. Пользователь вводит число. Программа завершится, когда пользователь введет значение больше 100. Ответ: Вы ввели число больше 100

while True:
    num = int(input("Enter a number: "))
    if num < 100:
        print(num)
    elif num > 100:
        break
    else:
        print("Error")