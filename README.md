# Thiranex Internship - Task 1

## Data Cleaning & Visualization

### Objective

The objective of this project is to clean, analyze, and visualize supermarket sales data using Python.

---

## Dataset

The dataset contains **1,000 supermarket transactions** and **17 columns**.

The dataset includes information such as:

- Invoice ID
- Branch
- City
- Customer Type
- Gender
- Product Line
- Unit Price
- Quantity
- Tax 5%
- Total Sales
- Date
- Time
- Payment Method
- COGS
- Gross Margin Percentage
- Gross Income
- Customer Rating

---

## Data Cleaning

The following data-cleaning steps were performed using Pandas.

### 1. Missing Values

Missing values were checked before and after cleaning.

**Result:** No missing values were found.

### 2. Duplicate Records

Duplicate rows were checked and removed.

**Result:** No duplicate rows were found.

### 3. Date Conversion

The `Date` column was converted into a proper datetime format to enable time-based analysis.

### 4. Outlier Detection

The Interquartile Range (IQR) method was used to detect outliers in numerical columns.

A total of **9 high-value transactions** were identified as outliers in the `Total` column.

After investigation, these transactions were found to be legitimate supermarket transactions with a quantity of 10. Therefore, the outliers were **retained rather than removed**.

---

## Data Analysis

The following analyses were performed:

- Total sales by product line
- Total sales by branch
- Total sales by customer type
- Total sales by gender
- Daily sales trend
- Payment method usage
- Average transaction value by product line
- Sales distribution by product line

---

## Visualizations

The project uses:

- **Pandas** for data manipulation and analysis
- **Matplotlib** for data visualization
- **Seaborn** for statistical visualization

The following visualizations were created:

1. Total Sales by Product Line
2. Total Sales by Branch
3. Total Sales by Customer Type
4. Total Sales by Gender
5. Daily Sales Trend
6. Sales Distribution by Product Line
7. Payment Method Usage
8. Average Transaction Value by Product Line

All visualizations are saved in the `figures` folder.

---

## Key Findings

### Product Line

**Food and beverages** generated the highest total sales.

**Health and beauty** generated the lowest total sales.

### Branch Performance

**Branch C** generated the highest total sales among the three branches.

### Customer Type

**Member customers** generated higher total sales than normal customers.

### Gender

Female customers generated higher total sales than male customers in this dataset.

### Payment Method

**E-wallet** was the most frequently used payment method, followed closely by cash.

### Sales Trend

Daily sales varied considerably throughout the analyzed period, with some days showing significantly higher sales than others.

### Average Transaction Value

The average transaction value across the dataset was approximately **322.97**.

---

## Final Dataset Statistics

| Metric | Value |
|---|---:|
| Total Transactions | 1,000 |
| Number of Columns | 17 |
| Total Sales | 322,966.75 |
| Average Transaction Value | 322.97 |
| Missing Values | 0 |
| Duplicate Rows | 0 |
| Detected Outliers | 9 |

## Project Structure

```text
thiranex-task-1-data-cleaning/
│
├── task1.py
├── supermarket_sales - Sheet1.csv
├── cleaned_supermarket_sales.csv
├── README.md
│
└── figures/
    ├── 01_sales_by_product_line.png
    ├── 02_sales_by_branch.png
    ├── 03_sales_by_customer_type.png
    ├── 04_sales_by_gender.png
    ├── 05_daily_sales_trend.png
    ├── 06_sales_distribution_boxplot.png
    ├── 07_payment_method_usage.png
    └── 08_average_transaction_value.png

