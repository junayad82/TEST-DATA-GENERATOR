import random

users = []


def generate_user():
    names = ["Rahim", "Karim", "Hasan", "Sakib", "Nabil", "Rafi"]

    name = random.choice(names)
    age = random.randint(18, 60)
    phone = "017" + str(random.randint(10000000, 99999999))
    email = name.lower() + str(random.randint(100, 999)) + "@gmail.com"

    user = {
        "name": name,
        "age": age,
        "phone": phone,
        "email": email
    }

    users.append(user)

    print("\nUser generated successfully!")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"Phone: {user['phone']}")
    print(f"Email: {user['email']}")


def generate_multiple_users():
    amount = int(input("How many users do you want to generate? "))

    if amount <= 0:
        print("Invalid amount!")
        return

    for i in range(amount):
        names = ["Rahim", "Karim", "Hasan", "Sakib", "Nabil", "Rafi"]

        name = random.choice(names)
        age = random.randint(18, 60)
        phone = "017" + str(random.randint(10000000, 99999999))
        email = name.lower() + str(random.randint(100, 999)) + "@gmail.com"

        user = {
            "name": name,
            "age": age,
            "phone": phone,
            "email": email
        }

        users.append(user)

    print(f"\n{amount} users generated successfully!")


def view_users():
    if len(users) == 0:
        print("No users found!")
    else:
        print("\n====== GENERATED USERS ======")

        for index, user in enumerate(users, 1):
            print(f"\nUser {index}")
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            print(f"Phone: {user['phone']}")
            print(f"Email: {user['email']}")
            print("----------------------")


def search_user():
    search = input("Enter name or email to search: ")

    found = False

    for user in users:
        if (search.lower() in user["name"].lower()
                or search.lower() in user["email"].lower()):

            print("\nUser found!")
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            print(f"Phone: {user['phone']}")
            print(f"Email: {user['email']}")

            found = True

    if not found:
        print("User not found!")


def save_users():
    if len(users) == 0:
        print("No users to save!")
        return

    with open("test_data.txt", "w") as file:

        for index, user in enumerate(users, 1):
            file.write(f"User {index}\n")
            file.write(f"Name: {user['name']}\n")
            file.write(f"Age: {user['age']}\n")
            file.write(f"Phone: {user['phone']}\n")
            file.write(f"Email: {user['email']}\n")
            file.write("----------------------\n")

    print("Test data saved successfully!")


while True:

    print("\n====== TEST DATA GENERATOR ======")
    print("1. Generate One User")
    print("2. Generate Multiple Users")
    print("3. View Generated Users")
    print("4. Search User")
    print("5. Save Test Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_user()

    elif choice == "2":
        generate_multiple_users()

    elif choice == "3":
        view_users()

    elif choice == "4":
        search_user()

    elif choice == "5":
        save_users()

    elif choice == "6":
        print("Thank you for using Test Data Generator!")
        break

    else:
        print("Invalid choice!")