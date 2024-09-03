def calculator():
    while True:
        print("-------------------------------")
        print("\nSIMPLE CALCULATOR")
        print("Choose an operation :")
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Exit")
        print("-------------------------------")

        try:
            c = int(input("Enter your choice (1/2/3/4/5): "))
            
            if c == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if c == 1:
                operation = "Addition"
            elif c == 2:
                operation = "Subtraction"
            elif c == 3:
                operation = "Multiplication"
            elif c == 4:
                operation = "Division"
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
                continue

            print(f"\nYou chose: {operation}")
            a = float(input("Enter the 1st number: "))
            b = float(input("Enter the 2nd number: "))

            if c == 1:
                print("\nPerforming Addition...")
                result = a + b
            elif c == 2:
                print("\nPerforming Subtraction...")
                result = a - b
            elif c == 3:
                print("\nPerforming Multiplication...")
                result = a * b
            elif c == 4:
                if b != 0:
                    print("\nPerforming Division...")
                    result = a / b
                else:
                    print("Error: Division by zero is not allowed.")
                    continue

            print(f"\n{operation} Result: {result}")
        
        except ValueError:
            print("Error: Please enter valid numbers.")

calculator()
