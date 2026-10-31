import os
import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ["Date", "Product", "Region", "Quantity", "Amount"]


def load_and_clean_data(file_path):
    """Read CSV, remove duplicates, and skip invalid rows."""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None

    df = pd.read_csv(file_path, names=COLUMNS, header=None).drop_duplicates()
    valid_rows = []

    for index, row in df.iterrows():
        try:
            quantity = int(row["Quantity"])
            amount = float(row["Amount"])
            date = pd.to_datetime(row["Date"], errors="raise")

            if quantity < 0 or amount < 0:
                raise ValueError

            row["Date"] = date
            row["Quantity"] = quantity
            row["Amount"] = amount
            valid_rows.append(row)

        except (ValueError, TypeError):
            print(f"Row {index + 1} skipped: invalid Amount '{row['Amount']}'")

    if not valid_rows:
        return None

    return pd.DataFrame(valid_rows)


def show_summary(df):
    total_revenue = int(df["Amount"].sum())
    transactions = len(df)
    units_sold = int(df["Quantity"].sum())

    if transactions == 1:
        top_product = df.iloc[0]["Product"]
        print(
            f"Total Revenue: {total_revenue} | "
            f"Transactions: {transactions} | Top product: {top_product}"
        )
    else:
        print(
            f"Total Revenue: {total_revenue} | "
            f"Transactions: {transactions} | Units sold: {units_sold}"
        )


def analyze_and_plot(df):
    product_sales = df.groupby("Product")["Amount"].sum()
    region_sales = df.groupby("Region")["Amount"].sum()

    print(" | ".join(
        f"{product}: {int(amount)}"
        for product, amount in product_sales.sort_values(ascending=False).items()
    ))
    print(" | ".join(
        f"{region}: {int(amount)}"
        for region, amount in region_sales.sort_values(ascending=False).items()
    ))

    print("\nTop 5 Selling Products:")
    top_products = df.groupby("Product")["Quantity"].sum().nlargest(5)
    for product, quantity in top_products.items():
        print(f"{product}: {int(quantity)} units")

    plt.figure(figsize=(7, 4))
    region_sales.plot(kind="bar")
    plt.title("Region-wise Sales")
    plt.xlabel("Region")
    plt.ylabel("Amount")
    plt.tight_layout()

    date_sales = df.groupby("Date")["Amount"].sum().sort_index()
    plt.figure(figsize=(7, 4))
    date_sales.plot(kind="line", marker="o")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.tight_layout()

    print("\nBar chart 'Region-wise Sales' displayed")
    plt.show()


def main():
    df = load_and_clean_data("sales.csv")

    if df is None or df.empty:
        print("No valid sales data available.")
        return

    print("\n--- Menu ---")
    print("1. Summary")
    print("2. Group by Product & Region")

    choice = input("Enter choice (1 or 2): ").strip()
    print()

    if choice == "1":
        show_summary(df)
    elif choice == "2":
        analyze_and_plot(df)
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
