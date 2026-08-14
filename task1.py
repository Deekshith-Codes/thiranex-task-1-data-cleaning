import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# THIRANEX INTERNSHIP - TASK 1
# Data Cleaning & Visualization
# ============================================================

print("=" * 60)
print("THIRANEX INTERNSHIP - TASK 1")
print("Data Cleaning & Visualization")
print("=" * 60)


# ------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------

INPUT_FILE = "supermarket_sales - Sheet1.csv"
OUTPUT_FILE = "cleaned_supermarket_sales.csv"
FIGURE_DIR = "figures"

# Create figures folder if it doesn't exist
os.makedirs(FIGURE_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("\n--- DATASET INFORMATION ---")
print("Rows and columns:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ------------------------------------------------------------
# 3. DATE CONVERSION
# ------------------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


# ------------------------------------------------------------
# 4. MISSING VALUE CHECK
# ------------------------------------------------------------

print("\n--- MISSING VALUES ---")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Remove rows containing missing values
df = df.dropna()

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 5. DUPLICATE CHECK
# ------------------------------------------------------------

print("\n--- DUPLICATE CHECK ---")

duplicates_before = df.duplicated().sum()

print("Duplicate rows before cleaning:", duplicates_before)

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print("Duplicate rows after cleaning:", duplicates_after)


# ------------------------------------------------------------
# 6. DESCRIPTIVE STATISTICS
# ------------------------------------------------------------

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())


# ------------------------------------------------------------
# 7. SALES ANALYSIS
# ------------------------------------------------------------

print("\n--- SALES BY PRODUCT LINE ---")

sales_by_product = (
    df.groupby("Product line")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_product)


print("\n--- SALES BY BRANCH ---")

sales_by_branch = (
    df.groupby("Branch")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_branch)


print("\n--- SALES BY CUSTOMER TYPE ---")

sales_by_customer = (
    df.groupby("Customer type")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_customer)


print("\n--- SALES BY GENDER ---")

sales_by_gender = (
    df.groupby("Gender")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_gender)


print("\n--- PAYMENT METHOD USAGE ---")

payment_counts = df["Payment"].value_counts()

print(payment_counts)


# ------------------------------------------------------------
# 8. VISUALIZATION 1
# Total Sales by Product Line
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sales_by_product.sort_values().plot(kind="barh")

plt.title("Total Sales by Product Line")
plt.xlabel("Total Sales")
plt.ylabel("Product Line")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "01_sales_by_product_line.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 9. VISUALIZATION 2
# Total Sales by Branch
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sales_by_branch.sort_values().plot(kind="bar")

plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "02_sales_by_branch.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 10. VISUALIZATION 3
# Total Sales by Customer Type
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sales_by_customer.sort_values().plot(kind="bar")

plt.title("Total Sales by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "03_sales_by_customer_type.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 11. VISUALIZATION 4
# Total Sales by Gender
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sales_by_gender.sort_values().plot(kind="bar")

plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "04_sales_by_gender.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 12. VISUALIZATION 5
# Daily Sales Trend
# ------------------------------------------------------------

daily_sales = df.groupby("Date")["Total"].sum()

plt.figure(figsize=(12, 6))

daily_sales.plot()

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "05_daily_sales_trend.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 13. VISUALIZATION 6
# Sales Distribution by Product Line
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Product line",
    y="Total"
)

plt.title("Sales Distribution by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "06_sales_distribution_boxplot.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 14. VISUALIZATION 7
# Payment Method Usage
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

payment_counts.plot(kind="bar")

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "07_payment_method_usage.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 15. VISUALIZATION 8
# Average Transaction Value by Product Line
# ------------------------------------------------------------

avg_sales_product = (
    df.groupby("Product line")["Total"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 6))

avg_sales_product.plot(kind="barh")

plt.title("Average Transaction Value by Product Line")
plt.xlabel("Average Total")
plt.ylabel("Product Line")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURE_DIR, "08_average_transaction_value.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------------------------
# 16. OUTLIER DETECTION
# ------------------------------------------------------------

print("\n--- OUTLIER DETECTION ---")

numeric_columns = df.select_dtypes(include="number").columns

outlier_summary = {}

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    outlier_summary[column] = len(outliers)

    print(f"{column}: {len(outliers)} outliers")


# ------------------------------------------------------------
# 17. INVESTIGATE TOTAL SALES OUTLIERS
# ------------------------------------------------------------

Q1 = df["Total"].quantile(0.25)
Q3 = df["Total"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

total_outliers = df[
    (df["Total"] < lower_bound) |
    (df["Total"] > upper_bound)
]

print("\n--- TOTAL SALES OUTLIERS ---")

print(
    total_outliers[
        ["Invoice ID", "Product line", "Quantity", "Total"]
    ]
)

print("\nOutliers detected:", len(total_outliers))

print(
    "Outliers were retained because they represent "
    "valid supermarket transactions."
)


# ------------------------------------------------------------
# 18. SAVE CLEANED DATASET
# ------------------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\n--- EXPORT ---")
print(f"Cleaned dataset saved as: {OUTPUT_FILE}")


# ------------------------------------------------------------
# 19. FINAL PROJECT SUMMARY
# ------------------------------------------------------------

total_sales = df["Total"].sum()

average_transaction = df["Total"].mean()

best_product = sales_by_product.idxmax()

best_branch = sales_by_branch.idxmax()

most_used_payment = payment_counts.idxmax()


print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"Final dataset size: {df.shape}")
print(f"Total sales: {total_sales:.2f}")
print(f"Average transaction value: {average_transaction:.2f}")
print(f"Best performing product line: {best_product}")
print(f"Best performing branch: {best_branch}")
print(f"Most used payment method: {most_used_payment}")

print("\nFiles created:")
print(f"- {OUTPUT_FILE}")
print("- figures/01_sales_by_product_line.png")
print("- figures/02_sales_by_branch.png")
print("- figures/03_sales_by_customer_type.png")
print("- figures/04_sales_by_gender.png")
print("- figures/05_daily_sales_trend.png")
print("- figures/06_sales_distribution_boxplot.png")
print("- figures/07_payment_method_usage.png")
print("- figures/08_average_transaction_value.png")

print("=" * 60)
