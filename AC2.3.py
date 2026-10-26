def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                return age
            print("Age cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def welcome_user():
    user_name = input("Enter your name: ")
    print("Welcome", user_name)


def display_menu():
    print("1. View profile")
    print("2. Exit")


def save_user_data(age):
    with open("user_data.txt", "w") as file:
        file.write(str(age))


def main():
    welcome_user()
    age = get_user_age()
    display_menu()
    save_user_data(age)


if __name__ == "__main__":
    main()

# Temporary feature for testing Git revert