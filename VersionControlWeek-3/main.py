import random

password = ""
#change
#change 2
while True:
    length = int(input("Input desired password length: "))
    if 1 < length < 50:
        for i in range(length):
            random_int = random.randint(33, 126)
            password += chr(random_int)
        print(password)
        break
    else:
        print("Invalid length (2-49)")
        continue
        
k = input("Press any key to exit")

