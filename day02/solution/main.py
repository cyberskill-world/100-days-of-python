print("Welcome to the tip")

bill = float(input("What is the total bill amount: $"))
tip = int (input("how much tip: Perent(%)"))
split = int(input("how many people to split the bill: People "))

total = ("{:.2f}".format((((bill*(tip/100))+bill) / split)))

print(f"Each person should pay: {total} $")