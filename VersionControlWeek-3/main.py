import random
password = ""
for i in range(10):
    random_int = random.randint(0, 126)
    password += chr(random_int)
print(password, len(password))
