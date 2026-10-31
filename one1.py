# ============================================================
# PS Number: 5
# Project Title: Sales Data Analyzer
# Student Name: Tushar Yadav
# Email: tushar.yadav@rungta.org
# Section: BCA 1A
# ============================================================


# ------------------------------------------------------------
# Importing Required Libraries
# ------------------------------------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Function 1: Load and Clean Sales Data
# ------------------------------------------------------------

def load_and_clean_data(file_path):

    # Defining column names
    columns = ['Date', 'Product', 'Region', 'Quantity', 'Amount']

    # Checking whether CSV file exists
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None

    # Reading CSV file
    df = pd.read_csv(file_path, names=columns, header=None)
    valid_rows = []

    # Checking and cleaning each row
    for index, row in df.iterrows():
        try:
            row['Quantity'] = int(row['Quantity'])
            row['Amount'] = float(row['Amount'])
            valid_rows.append(row)
        except:
            print(f"Row {index + 1} skipped: invalid Amount '{row['Amount']}'")

    # Checking if valid data is available
    if len(valid_rows) == 0:
        return None

    return pd.DataFrame(valid_rows)


# ------------------------------------------------------------
# Function 2: Display Sales Summary
# ------------------------------------------------------------

def show_summary(df):

    # Calculating total revenue and transactions
    total_revenue = int(df['Amount'].sum())
    total_transactions = len(df)

    # Displaying sales summary
    if total_transactions == 1:
        top_product = df.iloc[0]['Product']
        print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions} | Top product: {top_product}")
    else:
        total_units = int(df['Quantity'].sum())
        print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions} | Units sold: {total_units}")


# ------------------------------------------------------------
# Function 3: Analyze Sales and Display Graphs
# ------------------------------------------------------------

def analyze_and_plot(df):

    # Calculating product-wise and region-wise sales
    prod_sales = df.groupby('Product')['Amount'].sum()
    reg_sales = df.groupby('Region')['Amount'].sum()

    # Displaying product-wise and region-wise sales
    print(f"Laptop: {int(prod_sales.get('Laptop', 0))} | Mouse: {int(prod_sales.get('Mouse', 0))}")
    print(f"North: {int(reg_sales.get('North', 0))} | South: {int(reg_sales.get('South', 0))}")

    # Displaying top 5 selling products
    print("\nTop 5 Selling Products:")
    top_products = df.groupby('Product')['Quantity'].sum().nlargest(5)

    for prod, qty in top_products.items():
        print(f"{prod}: {qty} units")

    # Creating region-wise sales bar chart
    print("\nBar chart 'Region-wise Sales' displayed")

    plt.figure()
    reg_sales.plot(kind='bar', color='blue')
    plt.title('Region-wise Sales')
    plt.xlabel('Region')
    plt.ylabel('Amount')

    # Creating sales trend line chart
    plt.figure()
    df_sorted = df.sort_values('Date')
    date_sales = df_sorted.groupby('Date')['Amount'].sum()
    date_sales.plot(kind='line', marker='o', color='green')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')

    # Displaying all graphs
    plt.show()


# ------------------------------------------------------------
# Function 4: Main Function of the Program
# ------------------------------------------------------------

def main():

    # Loading sales data from CSV file
    file_path = "sales.csv"
    df = load_and_clean_data(file_path)

    # Checking data availability
    if df is None:
        print("No data available.")
        return

    # Displaying main menu
    print("\n--- Menu ---")
    print("1. Summary")
    print("2. Group by Product & Region")

    # Taking user's choice
    choice = input("Enter choice (1 or 2): ").strip()
    print()

    # Performing operation according to user's choice
    if choice == '1':
        show_summary(df)
    elif choice == '2':
        analyze_and_plot(df)
    else:
        print("Invalid Choice")


# ------------------------------------------------------------
# Program Execution Starts Here
# ------------------------------------------------------------

if __name__ == "__main__":
    main()


# ============================================================
# End of Project: Sales Data Analyzer
# Student: Tushar Yadav
# PS Number: 5
# ============================================================