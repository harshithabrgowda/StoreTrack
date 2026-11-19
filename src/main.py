from menu import display_menu, get_menu_choice
from data_structures import display_products, add_product, search_product, view_stock
from billing import new_sale
from analysis import (
    sales_analysis,
    daily_revenue,
    monthly_revenue,
    best_selling_products,
    category_wise_sales
)
from visualization import (
    daily_revenue_chart,
    top_products_chart,
    dashboard_chart
)


def main():
    while True:
        display_menu()

        choice = get_menu_choice()

        if choice == 1:
            display_products()

        elif choice == 2:
            add_product()

        elif choice == 3:
            new_sale()

        elif choice == 4:
         view_stock()

        elif choice == 5:
            search_product()

        elif choice == 6:
            sales_analysis()
            daily_revenue()
            monthly_revenue()
            best_selling_products()
            category_wise_sales()

        elif choice == 7:
            daily_revenue_chart()
            top_products_chart()
            dashboard_chart()

        elif choice == 8:
            print("Thank you for using StoreTrack!")
            break


if __name__ == "__main__":
    main()