import csv
import random
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALES_FILE = os.path.join(BASE_DIR, "data", "sales.csv")


def generate_sample_sales():

    products = [
        ("P001", "Rice", "Grocery", 60.00),
        ("P002", "Milk", "Dairy", 30.00),
        ("P003", "Bread", "Bakery", 40.00),
        ("P004", "Sugar", "Grocery", 45.00),
        ("P005", "Soap", "Personal Care", 35.00),
        ("P006", "Shampoo", "Personal Care", 120.00)
    ]

    start_date = datetime.now() - timedelta(days=29)

    rows = []

    for i in range(1, 121):

        product = random.choice(products)

        product_id = product[0]
        product_name = product[1]
        category = product[2]
        price = product[3]

        quantity = random.randint(1, 5)

        item_total = price * quantity

        if item_total >= 1000:
            discount_rate = 10
        elif item_total >= 500:
            discount_rate = 5
        else:
            discount_rate = 0

        discount = item_total * discount_rate / 100

        after_discount = item_total - discount

        gst = after_discount * 5 / 100

        final_amount = after_discount + gst

        sale_date = (
            start_date + timedelta(days=random.randint(0, 29))
        ).strftime("%Y-%m-%d")

        rows.append([
            sale_date,
            f"INV{i:03d}",
            product_id,
            product_name,
            category,
            price,
            quantity,
            item_total,
            item_total,
            discount,
            gst,
            final_amount
        ])

    with open(SALES_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Invoice No",
            "Product ID",
            "Product Name",
            "Category",
            "Price",
            "Quantity",
            "Item Total",
            "Subtotal",
            "Discount",
            "GST",
            "Final Amount"
        ])

        writer.writerows(rows)

    print("120 sample sales records generated successfully!")


if __name__ == "__main__":
    generate_sample_sales()