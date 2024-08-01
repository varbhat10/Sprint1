import webbrowser

users = {}
images = {}


def register_user():
    print("\n=== Registration ===")
    email = input("Enter your email (e.g., user@example.com): ").strip()
    if "@" not in email or "." not in email:
        print("Error: Please enter a valid email address.")
        return None

    password = input("Enter your password: ").strip()
    if not password:
        print("Error: Password cannot be empty.")
        return None

    if email in users:
        print("Error: Email already registered.")
        return None
    else:
        users[email] = password
        print("Registration successful!")
        return email


def display_cat_image_of_the_day():
    print("\n=== Cat Image of the Day ===")
    cat_image_url = "https://www.freeimages.com/search/cat"
    print("Opening your browser to view the cat image of the day...")
    webbrowser.open(cat_image_url)
    print("If the browser doesn't open automatically, please visit the following link:")
    print(cat_image_url)


def show_about():
    print("\n=== ABOUT ===")
    print("This application allows users to register and view a cat image of the day.")


def show_menu():
    print("\nWelcome to the Cat Image Collection App")
    print("Please choose an option:")
    print("1. Register")
    print("2. Show cat of the day")
    print("3. About")
    print("4. Quit")
    print("Enter the option number or the corresponding word (e.g., '1' or 'register').")


def main():
    registered_user = None
    show_menu()

    while True:
        choice = input("\nEnter/Register/Show/About/Q: ").strip().lower()

        if choice in ['1', 'register']:
            registered_user = register_user()
        elif choice in ['2', 'show']:
            if registered_user:
                display_cat_image_of_the_day()
            else:
                print("Please register first to view the cat image of the day.")
        elif choice in ['3', 'about']:
            show_about()
        elif choice in ['4', 'q', 'quit']:
            print("Thank you for using the Cat Image Collection App!")
            break
        else:
            print("Invalid choice. Please enter a valid option number or word.")

        show_menu()  # Display the menu options again after each action


if __name__ == "__main__":
    main()
