# Sales Data Analyzer

Python project for analysing sales data stored in a CSV file using **Pandas** and **Matplotlib**.

## Problem Statement

Analyse a sales CSV file to find total revenue, best-selling products, and region-wise performance using grouping, then visualise the results.

**Language:** Python 3  
**Concepts:** Pandas, CSV, Matplotlib, Grouping

## CSV Format

The program expects `sales.csv` with these columns (without a header):

```text
Date,Product,Region,Quantity,Amount
```

Example:

```text
2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,5000
2026-08-03,Laptop,South,1,50000
```

## Features

- Reads sales data from CSV using Pandas
- Removes duplicate rows
- Skips invalid Amount/Quantity rows
- Calculates total revenue, transaction count, and units sold
- Finds the top product
- Groups sales by product and region
- Displays the top 5 selling products
- Creates a region-wise bar chart
- Creates a sales-trend line chart
- Menu-driven console interface

## Project Structure

```text
Sales-Data-Analyzer/
├── README.md
├── requirements.txt
├── sales.csv
└── one.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python one.py
```

## Menu

```text
=== SALES DATA ANALYZER ===
1. Summary
2. Group by Product & Region
3. Exit
```

## Expected Result for Provided CSV

Summary:

```text
Total Revenue: 155000 | Transactions: 3 | Units sold: 13
Top product: Laptop
```

Grouped sales:

```text
Product-wise Sales:
Laptop: 150000
Mouse: 5000

Region-wise Sales:
North: 100000
South: 55000
```

## Requirements

- Python 3
- pandas
- matplotlib
