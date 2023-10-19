import random
print("Welcome to our password generator")
print()
letters_and_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@£$%^&*-_#().,/;:"

number_of_passwords = int(input("Enter how many passwords to give: "))

lenght_of_passwords = int(input("Enter what to be the lenght of the password: "))

for number in range(number_of_passwords):
    passwords = ""

    for lenght in range(lenght_of_passwords):
        passwords += random.choice(letters_and_numbers)

    print(passwords)
