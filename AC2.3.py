def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                return age
            print("Age cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")

age = get_user_age()
print("Your age is:", age)