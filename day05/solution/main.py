import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= (input("How many letters would you like in your password: "))
nr_symbols = (input("How many symbols would you like: "))
nr_numbers = (input("How many numbers would you like: "))

if not nr_letters.isdigit() or not nr_numbers.isdigit() or not nr_symbols.isdigit():
    print("Invalid value, enter a number instead.")
else:
    if int(nr_letters) <= 0 or int(nr_numbers) <= 0 or int(nr_symbols) <= 0:
        print("Please enter a positive number greater than 0.")
    else:
        password = []

        for i in range(0, int(nr_letters)):
            random_letter = random.randint(0,51)
            password.append(letters[random_letter])

        for i in range(0, int(nr_numbers)):
            radom_number = random.randint(0,9)
            password.append(numbers[radom_number])

        for i in range(0, int(nr_symbols)):
            random_symbols = random.randint(0,8)
            password.append(symbols[random_symbols])

        random.shuffle(password)
        print(f"here is your password: {'_'.join(password)}")

        if len(password) <= 6:
            print("Your password is weak, try to include at least 8 characters for a stronger password.")
        elif len(password) == 7:
            print("Your password is medium, try to include at least 8 characters for a stronger password.")
        else:
            print("Your password is strong.")
