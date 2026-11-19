import csv
import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SALES_FILE = os.path.join(BASE_DIR, "data", "sales.csv")
PRODUCTS_FILE = os.path.join(BASE_DIR, "data", "products.json")


def save_sale(invoice_no, cart, subtotal, discount_amount, gst_amount, final_amount):

    file_exists = os.path.exists(SALES_FILE)

    with open(SALES_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
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

        sale_date = datetime.now().strftime("%Y-%m-%d")

        for item in cart:
            writer.writerow([
                sale_date,
                invoice_no,
                item["product_id"],
                item["name"],
                item["category"],
                item["price"],
                item["quantity"],
                item["total"],
                subtotal,
                discount_amount,
                gst_amount,
                final_amount
            ])


def save_products(products):

    with open(PRODUCTS_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)


def load_products():

    if os.path.exists(PRODUCTS_FILE):

        with open(PRODUCTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {}