import random

password = ""

while True:
    length = int(input("Input desired password length: "))
    if 1 < length < 50:
        for i in range(length):
            random_int = random.randint(0, 126)
            password += chr(random_int)
        print(password, len(password))
        break
    else:
        print("Invalid length (2-49)")
        continue
        
