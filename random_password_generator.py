from random import choice

len_of_password=8

valid_chars_for_password='abcdefghijklmnopqrstuvwxyz!@#%^&*()?1234567890'


password = []

for each_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))

print("".join(password))
