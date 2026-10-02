import random

print("password generator")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = " "

for i in range(8):
    password += random.choice(letters)
    
print("generated password:", password)b
 
 