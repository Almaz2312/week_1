ssd_drive = int(input("Размер SSD диска (GB): "))
hdd_drive = int(input("Размер HDD диска (TB): "))
ram = int(input("RAM (GB): "))
price = int(input("Стоимость (USD): "))
if (ssd_drive >= 256 or hdd_drive >= 1) and (ram >= 4) and (ram <= 8) and (price <= 1000):
    print("Имеется в наличии")
else:
    print("Не имеется в наличии")
