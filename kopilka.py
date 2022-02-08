# Необходимо ввести сумму, которую нужно накопить. Далее вводить значения, пока не накопится нужная сумма.
goal = int(input("Enter desired sum: "))
total = []
while sum(total) <= goal:
    num = int(input("Quantity of money put "))
    total.append(num)
    print(num)
