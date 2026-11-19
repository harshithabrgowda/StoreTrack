def display_menu():
    print("\n" + "=" * 45)
    print("              STORETRACK")
    print("      RETAIL SALES MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. View Products")
    print("2. Add Product")
    print("3. New Sale")
    print("4. View Stock")
    print("5. Search Product")
    print("6. Sales Analysis")
    print("7. Generate Dashboard")
    print("8. Exit")

    print("=" * 45)


def get_menu_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= 8:
                return choice

            print("Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")