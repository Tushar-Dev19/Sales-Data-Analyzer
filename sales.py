import os
import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ["Date", "Product", "Region", "Quantity", "Amount"]


def load_and_clean_data(file_path):
    """Load sales CSV, remove duplicates, and skip invalid rows."""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None

    df = pd.read_csv(file_path, names=COLUMNS, header=None).drop_duplicates()
    valid_rows = []

    for index, row in df.iterrows():
        try:
            quantity = int(row["Quantity"])
            amount = float(row["Amount"])
            if quantity < 0 or amount < 0:
                raise ValueError

            row["Quantity"] = quantity
            row["Amount"] = amount
            valid_rows.append(row)
        except (ValueError, TypeError):
            print(f"Row {index + 1} skipped: invalid Amount/Quantity")

    if not valid_rows:
        return None

    clean_df = pd.DataFrame(valid_rows)
    clean_df["Date"] = pd.to_datetime(clean_df["Date"], errors="coerce")
    clean_df = clean_df.dropna(subset=["Date"])
    return clean_df


def show_summary(df):
    total_revenue = int(df["Amount"].sum())
    transactions = len(df)
    units_sold = int(df["Quantity"].sum())

    product_sales = df.groupby("Product")["Amount"].sum()
    top_product = product_sales.idxmax()

    print(f"Total Revenue: {total_revenue} | Transactions: {transactions} | Units sold: {units_sold}")
    print(f"Top product: {top_product}")


def analyze_and_plot(df):
    product_sales = df.groupby("Product")["Amount"].sum().sort_values(ascending=False)
    region_sales = df.groupby("Region")["Amount"].sum().sort_values(ascending=False)
    top_products = df.groupby("Product")["Quantity"].sum().nlargest(5)

    print("\nProduct-wise Sales:")
    for product, amount in product_sales.items():
        print(f"{product}: {int(amount)}")

    print("\nRegion-wise Sales:")
    for region, amount in region_sales.items():
        print(f"{region}: {int(amount)}")

    print("\nTop 5 Selling Products:")
    for product, quantity in top_products.items():
        print(f"{product}: {int(quantity)} units")

    plt.figure(figsize=(7, 4))
    region_sales.plot(kind="bar")
    plt.title("Region-wise Sales")
    plt.xlabel("Region")
    plt.ylabel("Sales Amount")
    plt.tight_layout()

    daily_sales = df.groupby("Date")["Amount"].sum().sort_index()
    plt.figure(figsize=(7, 4))
    daily_sales.plot(kind="line", marker="o")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales Amount")
    plt.tight_layout()

    print("\nBar chart 'Region-wise Sales' displayed")
    print("Line chart 'Sales Trend Over Time' displayed")
    plt.show()


def main():
    df = load_and_clean_data("sales.csv")

    if df is None or df.empty:
        print("No valid sales data available.")
        return

    while True:
        print("\n=== SALES DATA ANALYZER ===")
        print("1. Summary")
        print("2. Group by Product & Region")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            analyze_and_plot(df)
        elif choice == "3":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
