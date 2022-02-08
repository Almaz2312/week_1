ram = int(input("RAM: "))
hard_drive_ssd = int(input("Hard drive ssd (mb): "))
hard_drive_hdd = int(input("Hard drive hdd (tb)x`: "))
price = int(input("price: "))
if ram > 3 and hard_drive_ssd > 255 and price < 1000:
    print("Good")
elif ram > 3 and hard_drive_hdd > 1 and price < 1000:
    print("Good")
else:
    print("Not interested")
