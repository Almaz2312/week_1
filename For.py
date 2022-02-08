#1  Вывести имя 10 раз через for
 for i in range(10):
     print("Almaz")

#2  Вывести на экран числа от 1 до 100 через for
 for i in range(1,101):
     print(i)

#3   Вывести на экран все четные числа от 1 до 100 через for
for i in range(2,101,2):
    print(i)

#4   Вывести на экран все числа от 1 до 100 кратные 4 через for
for i in range(1,101):
    if i % 4 == 0:
        print(i)