import random

password = ""
#change
#change 2
while True:
    length = int(input("Input desired password length: "))
    print("Do you want password to include: ")
    while True:
        upper_ = input("Uppercase letters? (Y/N): ")
        if upper_.upper() == "Y":
            upperBool = True
            break
        elif upper_.upper() == "N":
            upperBool = False
            break
        else:
            print("Invalid input.")
            continue
    while True:
        lower = input("Lowercase letters? (Y/N): ")
        if lower.upper() == "Y":
            lowerBool = True
            break
        elif lower.upper() == "N":
            lowerBool = False
            break
        else:
            print("Invalid input.")
            continue
    while True:
        digits = input("Digits? (Y/N): ")
        if digits.upper() == "Y":
            digitsBool = True
            break
        elif digits.upper() == "N":
            digitsBool = False
            break
        else:
            print("Invalid input.")
            continue
    while True:
        special = input("Special characters? (Y/N): ")
        if special.upper() == "Y":
            specialBool = True
            break
        elif special.upper() == "N":
            specialBool = False
            break
        else:
            print("Invalid input.")
            continue

    randomString = ""
    if upperBool:
        randomString += str(random.randint(65, 90))
    if lowerBool:
        if randomString != "":
            randomString += ", "
        randomString += str(random.randint(97, 122))
    if digitsBool:
        if randomString != "":
            randomString += ", "
        randomString += str(random.randint(48, 57))
    if specialBool:
        if randomString != "":
            randomString += ", "
        randomString += str(random(random.randint(33, 47), random.randint(58, 64), random.randint(91, 96), random.randint(123, 126)))

    if 1 < length < 50:
        for i in range(length):
            random_int = random.choice(randomString)
            password += chr(int(random_int))
        print("Password: ", password, len(password))
        break
    else:
        print("Invalid length (2-49)")
        continue
        
k = input("Press any key to exit")

