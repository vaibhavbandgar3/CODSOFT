import random
import string

def password_generator():
    print("Choose the length of the password:")
    print("\t1. 6 characters")
    print("\t2. 8 characters")
    print("\t3. 16 characters")
    print("\t4. Custom length")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            l = 6
        elif choice == 2:
            l = 8
        elif choice == 3:
            l = 16
        elif choice == 4:
            l = int(input("Enter the custom length of the password: "))
            if l <= 0:
                print("Please enter a valid length greater than 0.")
                return
        else:
            print("Invalid choice\n\tPlease select a valid option (1/2/3/4).")
            return
        
        print("")
        print("Choose the strength of the password:")
        print("\t1. Easy")
        print("\t2. Moderate")
        print("\t3. Hard")

        strength = int(input("Enter your choice (1/2/3): "))

        if strength == 1:
            a = string.ascii_letters
        elif strength == 2:
            a = string.ascii_letters + string.digits
        elif strength == 3:
            a = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid choice\nPlease select a valid option (1/2/3).")
            return

        x = "".join(random.choice(a) for i in range(l))
        print("Password is : ", x)

    except ValueError:
        print("ENTER VALID NUMBER")

password_generator()
