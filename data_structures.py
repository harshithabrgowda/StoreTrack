from file_handler import load_products, save_products

# StoreTrack Product Catalogue
products = load_products()


def display_products():
    print("\n=============================================")
    print("              PRODUCT CATALOGUE")
    print("=============================================")

    for product_id, product in products.items():
        print(f"ID       : {product_id}")
        print(f"Name     : {product['name']}")
        print(f"Category : {product['category']}")
        print(f"Price    : ₹{product['price']:.2f}")
        print(f"Stock    : {product['stock']}")
        print("---------------------------------------------")


def add_product():
    print("\n=============================================")
    print("                ADD PRODUCT")
    print("=============================================")

    product_id = input("Enter Product ID: ").strip().upper()

    if product_id in products:
        print("Product ID already exists.")
        return

    name = input("Enter Product Name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    category = input("Enter Category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        price = float(input("Enter Price: "))

        if price <= 0:
            print("Price must be greater than 0.")
            return

        stock = int(input("Enter Stock: "))

        if stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Invalid price or stock. Please enter valid numbers.")
        return

    products[product_id] = {
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    save_products(products)

    print("\nProduct added successfully!")


def search_product():
    print("\n=============================================")
    print("              SEARCH PRODUCT")
    print("=============================================")

    product_id = input("Enter Product ID: ").strip().upper()

    if product_id in products:
        product = products[product_id]

        print("\nProduct Found!")
        print("---------------------------------------------")
        print(f"ID       : {product_id}")
        print(f"Name     : {product['name']}")
        print(f"Category : {product['category']}")
        print(f"Price    : ₹{product['price']:.2f}")
        print(f"Stock    : {product['stock']}")
        print("---------------------------------------------")

    else:
        print("\nProduct not found.")


def view_stock():
    print("\n=============================================")
    print("                 STOCK")
    print("=============================================")

    print(f"{'ID':<8}{'Product':<20}{'Category':<18}{'Stock':<8}")
    print("-" * 54)

    for product_id, product in products.items():
        print(
            f"{product_id:<8}"
            f"{product['name']:<20}"
            f"{product['category']:<18}"
            f"{product['stock']:<8}"
        )

    print("=" * 54)


# Additional data structures used in StoreTrack

# Tuple - stores fixed product IDs
product_id_tuple = tuple(products.keys())

# Set - stores unique product categories
category_set = {product["category"] for product in products.values()}

# List comprehension - creates a list of product names
product_names = [product["name"] for product in products.values()]

# Dictionary comprehension - creates a dictionary of product prices
product_prices = {
    product_id: product["price"]
    for product_id, product in products.items()
}