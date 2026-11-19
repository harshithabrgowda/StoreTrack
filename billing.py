from data_structures import products
from file_handler import save_sale, save_products

invoice_number = 1


def new_sale():
    global invoice_number

    print("\n=============================================")
    print("                 NEW SALE")
    print("=============================================")
    print(f"Invoice No: INV{invoice_number:03d}")

    cart = []

    while True:
        product_id = input(
            "Enter Product ID (or type DONE to finish): "
        ).strip().upper()

        if product_id == "DONE":
            break

        if product_id not in products:
            print("Product not found. Please enter a valid Product ID.")
            continue

        product = products[product_id]

        print(f"Product: {product['name']}")
        print(f"Price: ₹{product['price']:.2f}")
        print(f"Available Stock: {product['stock']}")

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            if quantity > product["stock"]:
                print("Not enough stock available.")
                continue

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue

        item_total = product["price"] * quantity

        cart.append({
            "product_id": product_id,
            "name": product["name"],
            "category": product["category"],
            "price": product["price"],
            "quantity": quantity,
            "total": item_total
        })

        print(f"{product['name']} added to cart.")
        print(f"Item Total: ₹{item_total:.2f}")

    if not cart:
        print("Cart is empty.")
        return

    print("\n=============================================")
    print("                  CART")
    print("=============================================")

    subtotal = 0

    for item in cart:
        print(
            f"{item['name']} | "
            f"Qty: {item['quantity']} | "
            f"₹{item['total']:.2f}"
        )

        subtotal += item["total"]

    print("---------------------------------------------")
    print(f"Subtotal: ₹{subtotal:.2f}")

    # Discount calculation
    if subtotal >= 1000:
        discount_rate = 10
    elif subtotal >= 500:
        discount_rate = 5
    else:
        discount_rate = 0

    discount_amount = subtotal * discount_rate / 100
    after_discount = subtotal - discount_amount

    print(f"Discount ({discount_rate}%): ₹{discount_amount:.2f}")
    print(f"Amount after discount: ₹{after_discount:.2f}")

    # GST calculation
    gst_rate = 5
    gst_amount = after_discount * gst_rate / 100
    final_amount = after_discount + gst_amount

    print(f"GST ({gst_rate}%): ₹{gst_amount:.2f}")
    print(f"Final Amount: ₹{final_amount:.2f}")

    # Update stock after the sale
    for item in cart:
        products[item["product_id"]]["stock"] -= item["quantity"]

    # Save updated products to JSON
    save_products(products)

    # Save sale to CSV
    save_sale(
        f"INV{invoice_number:03d}",
        cart,
        subtotal,
        discount_amount,
        gst_amount,
        final_amount
    )

    # Move to the next invoice number
    invoice_number += 1