import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALES_FILE = os.path.join(BASE_DIR, "data", "sales.csv")


def daily_revenue_chart():
    df = pd.read_csv(SALES_FILE)

    daily_sales = (
        df.groupby("Date")["Final Amount"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        daily_sales.index,
        daily_sales.values,
        marker="o"
    )

    plt.title("Daily Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue (₹)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def top_products_chart():
    df = pd.read_csv(SALES_FILE)

    product_sales = (
        df.groupby("Product Name")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        product_sales.index,
        product_sales.values
    )

    plt.title("Top-Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def dashboard_chart():
    df = pd.read_csv(SALES_FILE)

    # Daily revenue
    daily_sales = (
        df.groupby("Date")["Final Amount"]
        .sum()
        .sort_index()
    )

    # Top products
    product_sales = (
        df.groupby("Product Name")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    # Category-wise sales
    category_sales = (
        df.groupby("Category")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    # Price vs quantity
    price_quantity = df.groupby("Product Name").agg({
        "Price": "mean",
        "Quantity": "sum"
    })

    # Create 2 × 2 dashboard
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # 1. Daily Revenue
    axes[0, 0].plot(
        daily_sales.index,
        daily_sales.values,
        marker="o"
    )

    axes[0, 0].set_title("Daily Revenue")
    axes[0, 0].set_xlabel("Date")
    axes[0, 0].set_ylabel("Revenue (₹)")
    axes[0, 0].tick_params(axis="x", rotation=45)

    # 2. Top Products
    axes[0, 1].bar(
        product_sales.index,
        product_sales.values
    )

    axes[0, 1].set_title("Top-Selling Products")
    axes[0, 1].set_xlabel("Product")
    axes[0, 1].set_ylabel("Quantity Sold")
    axes[0, 1].tick_params(axis="x", rotation=45)

    # 3. Category Sales
    axes[1, 0].bar(
        category_sales.index,
        category_sales.values
    )

    axes[1, 0].set_title("Category-Wise Sales")
    axes[1, 0].set_xlabel("Category")
    axes[1, 0].set_ylabel("Quantity Sold")
    axes[1, 0].tick_params(axis="x", rotation=45)

    # 4. Price vs Quantity
    axes[1, 1].scatter(
        price_quantity["Price"],
        price_quantity["Quantity"]
    )

    axes[1, 1].set_title("Price vs Quantity Sold")
    axes[1, 1].set_xlabel("Average Price (₹)")
    axes[1, 1].set_ylabel("Quantity Sold")

    fig.suptitle(
        "StoreTrack Sales Dashboard",
        fontsize=16
    )

    plt.tight_layout()
    plt.show()