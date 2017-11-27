import time

while True:
    pwd = input("Enter password(Type 'done' to exit): " '\n'
    "> ")
    pwd_list = list(pwd)

# Variables used for validating the password
    val_for_alpha = None
    val_for_lower = None
    val_for_upper = None
    val_for_digit = None

    if pwd.lower() == "done":
        quit()

    if len(pwd) < 10:
        print("Your password is not long enough.")
        continue

    for x in pwd_list:
        if x.isalpha():
            val_for_alpha = "1"

            if x.islower():
                val_for_lower = "1"

            elif x.isupper():
                val_for_upper = "1"

        elif x.isdigit():
            val_for_digit = "1"

    time.sleep(1)
    print("Validating...")
    time.sleep(2)
    print()

    if val_for_alpha == "1" and val_for_lower == "1" and val_for_lower == "1" and val_for_upper == "1" and val_for_digit == "1":
        print("Great Password!")
        break

    else:
        print("Your password needs to contain at least one uppercase, one lowercase and one digit.")
        print()
