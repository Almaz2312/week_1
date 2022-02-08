type_of_car = input("input car: ")
milage = int(input("Milage: "))
year = int(input("Year: "))
owner = int(input("Number of owners: "))
side = input("Side of wheel: ")
price = int(input("Price: "))
color = input("Color: ")
if (type_of_car.lower() == "lexus" or type_of_car.lower() == "toyota") and (owner <= 2) and (year >= 2004):
    if price <= 10000 and milage <= 150000:
        print("Car available: lexus470")
    elif price <= 8000 and milage ==200000:
        print("Car available: toyota camry")
else:
    print("Cars are not available")
