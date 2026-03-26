import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

df = pd.read_csv(
    r"C:\C++ vs code\.vscode\projectdata.csv",
    sep="\t",
    encoding="latin1",
    engine="python",
    on_bad_lines="skip",
    quoting=3
)

print(df.head())
print(df.columns)


df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed')

print(df.dtypes)

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# -----------------------------
# Create Dashboard Layout
# -----------------------------
plt.figure(figsize=(22,16))

# -----------------------------
# 1 Sales Boxplot
# -----------------------------
plt.subplot(4,4,1)
sns.boxplot(x=df['Sales'])
plt.title("Sales Distribution")

# -----------------------------
# 2 Profit Boxplot
# -----------------------------
plt.subplot(4,4,2)
sns.boxplot(x=df['Profit'])
plt.title("Profit Distribution")

# -----------------------------
# 3 Discount Boxplot
# -----------------------------
plt.subplot(4,4,3)
sns.boxplot(x=df['Discount'])
plt.title("Discount Distribution")

# -----------------------------
# 4 Sales vs Profit
# -----------------------------
plt.subplot(4,4,4)
sns.scatterplot(x='Sales',y='Profit',data=df)
plt.title("Sales vs Profit")

# -----------------------------
# 5 Monthly Sales Trend
# -----------------------------
plt.subplot(4,4,5)
monthly_sales=df.groupby(['Year','Month'])['Sales'].sum()
monthly_sales.plot()
plt.title("Monthly Sales Trend")

# -----------------------------
# 6 Monthly Profit Trend
# -----------------------------
plt.subplot(4,4,6)
monthly_profit=df.groupby(['Year','Month'])['Profit'].sum()
monthly_profit.plot()
plt.title("Monthly Profit Trend")

# -----------------------------
# 7 Sales by Region
# -----------------------------
plt.subplot(4,4,7)
region_sales=df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar')
plt.title("Sales by Region")

# -----------------------------
# 8 Profit by Category
# -----------------------------
plt.subplot(4,4,8)
category_profit=df.groupby('Category')['Profit'].sum()
category_profit.plot(kind='bar')
plt.title("Profit by Category")

# -----------------------------
# 9 Sales Share Pie
# -----------------------------
plt.subplot(4,4,9)
category_sales=df.groupby('Category')['Sales'].sum()
category_sales.plot(kind='pie',autopct='%1.1f%%')
plt.ylabel("")
plt.title("Sales Share by Category")

# -----------------------------
# 10 Discount vs Profit
# -----------------------------
plt.subplot(4,4,10)
sns.scatterplot(x='Discount',y='Profit',data=df)
plt.title("Discount Impact on Profit")

# -----------------------------
# 11 Top Customers
# -----------------------------
plt.subplot(4,4,11)
top_customers=df.groupby('Customer Name')['Sales'].sum().nlargest(10)
top_customers.plot(kind='bar')
plt.title("Top Customers by Sales")

# -----------------------------
# 12 Profit Histogram
# -----------------------------
plt.subplot(4,4,12)
plt.hist(df['Profit'],bins=50)
plt.title("Profit Distribution Histogram")

# -----------------------------
# Layout
# -----------------------------
plt.suptitle("SUPERSTORE ANALYTICS DASHBOARD",fontsize=22)

plt.tight_layout()

plt.show()