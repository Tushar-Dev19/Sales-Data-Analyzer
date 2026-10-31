import os
import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
    columns = ['Date', 'Product', 'Region', 'Quantity', 'Amount']
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None

    df = pd.read_csv(file_path, names=columns, header=None)
    valid_rows = []
    
    for index, row in df.iterrows():
        try:
            row['Quantity'] = int(row['Quantity'])
            row['Amount'] = float(row['Amount'])
            valid_rows.append(row)
        except:
            print(f"Row {index + 1} skipped: invalid Amount '{row['Amount']}'")
            
    if len(valid_rows) == 0:
        return None
        
    return pd.DataFrame(valid_rows)

def show_summary(df):
    total_revenue = int(df['Amount'].sum())
    total_transactions = len(df)
    
    if total_transactions == 1:
        top_product = df.iloc[0]['Product']
        print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions} | Top product: {top_product}")
    else:
        total_units = int(df['Quantity'].sum())
        print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions} | Units sold: {total_units}")

def analyze_and_plot(df):
    prod_sales = df.groupby('Product')['Amount'].sum()
    reg_sales = df.groupby('Region')['Amount'].sum()
    
    print(f"Laptop: {int(prod_sales.get('Laptop', 0))} | Mouse: {int(prod_sales.get('Mouse', 0))}")
    print(f"North: {int(reg_sales.get('North', 0))} | South: {int(reg_sales.get('South', 0))}")
    
    print("\nTop 5 Selling Products:")
    top_products = df.groupby('Product')['Quantity'].sum().nlargest(5)
    for prod, qty in top_products.items():
        print(f"{prod}: {qty} units")
        
    print("\nBar chart 'Region-wise Sales' displayed")
    
    plt.figure()
    reg_sales.plot(kind='bar', color='blue')
    plt.title('Region-wise Sales')
    plt.xlabel('Region')
    plt.ylabel('Amount')
    
    plt.figure()
    df_sorted = df.sort_values('Date')
    date_sales = df_sorted.groupby('Date')['Amount'].sum()
    date_sales.plot(kind='line', marker='o', color='green')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    
    plt.show()

def main():
    file_path = "sales.csv"
    df = load_and_clean_data(file_path)
    
    if df is None:
        print("No data available.")
        return

    print("\n--- Menu ---")
    print("1. Summary")
    print("2. Group by Product & Region")
    
    choice = input("Enter choice (1 or 2): ").strip()
    print()
    
    if choice == '1':
        show_summary(df)
    elif choice == '2':
        analyze_and_plot(df)
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()