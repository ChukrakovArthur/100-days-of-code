import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

count_of_letters = int(input("How many letters would you like in your password?\n"))
count_of_symols = int(input("How many symbols would you like?\n"))
count_of_numbers = int(input("How many numbers would you like?\n"))
len_of_password = count_of_letters + count_of_numbers + count_of_symols

password = ''

for i in range(len_of_password):
    turn = random.randint(0, 2)
  
    if turn == 0:
        random_index = random.randint(0, len(letters) - 1)
    
        password += letters[random_index]
    elif turn == 1:
        random_index = random.randint(0, len(numbers) - 1)
    
        password += numbers[random_index]
    else:
        random_index = random.randint(0, len(symbols) - 1)
    
        password += symbols[random_index]
    
print(f"Your password is: {password}")