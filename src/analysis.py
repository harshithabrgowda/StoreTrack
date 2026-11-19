import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALES_FILE = os.path.join(BASE_DIR, "data", "sales.csv")


def sales_analysis():
    print("\n=============================================")
    print("              SALES ANALYSIS")
    print("=============================================")

    try:
        df = pd.read_csv(SALES_FILE)

        if df.empty:
            print("No sales data available.")
            return

        print(f"\nTotal Sales Records: {len(df)}")

        total_revenue = df["Final Amount"].sum()
        print(f"Total Revenue: ₹{total_revenue:.2f}")

        total_quantity = df["Quantity"].sum()
        print(f"Total Items Sold: {total_quantity}")

    except FileNotFoundError:
        print("Sales file not found.")


def daily_revenue():
    print("\n=============================================")
    print("              DAILY REVENUE")
    print("=============================================")

    try:
        df = pd.read_csv(SALES_FILE)

        if df.empty:
            print("No sales data available.")
            return

        daily_sales = (
            df.groupby("Date")["Final Amount"]
            .sum()
            .sort_index()
        )

        print("\nRevenue by Date:")
        print(daily_sales)

    except FileNotFoundError:
        print("Sales file not found.")


def monthly_revenue():
    print("\n=============================================")
    print("              MONTHLY REVENUE")
    print("=============================================")

    try:
        df = pd.read_csv(SALES_FILE)

        if df.empty:
            print("No sales data available.")
            return

        df["Date"] = pd.to_datetime(df["Date"])

        monthly_sales = (
            df.groupby(df["Date"].dt.to_period("M"))["Final Amount"]
            .sum()
            .sort_index()
        )

        print("\nRevenue by Month:")
        print(monthly_sales)

    except FileNotFoundError:
        print("Sales file not found.")


def best_selling_products():
    print("\n=============================================")
    print("          BEST-SELLING PRODUCTS")
    print("=============================================")

    try:
        df = pd.read_csv(SALES_FILE)

        if df.empty:
            print("No sales data available.")
            return

        best_sellers = (
            df.groupby("Product Name")["Quantity"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nProducts Sold:")
        print(best_sellers)

    except FileNotFoundError:
        print("Sales file not found.")


def category_wise_sales():
    print("\n=============================================")
    print("            CATEGORY-WISE SALES")
    print("=============================================")

    try:
        df = pd.read_csv(SALES_FILE)

        if df.empty:
            print("No sales data available.")
            return

        category_sales = (
            df.groupby("Category")["Quantity"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nSales by Category:")
        print(category_sales)

    except FileNotFoundError:
        print("Sales file not found.")