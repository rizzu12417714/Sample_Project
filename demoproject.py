import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv(
    "projectdata.csv",
    sep="\t",
    encoding="latin1",
    engine="python",
    on_bad_lines="skip",
    quoting=3
)

# -----------------------------
# Convert date columns
# -----------------------------
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed')

# -----------------------------
# Create extra columns
# -----------------------------
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby(['Year','Month'])['Sales'].sum()
monthly_profit = df.groupby(['Year','Month'])['Profit'].sum()

region_sales = df.groupby('Region')['Sales'].sum()
category_profit = df.groupby('Category')['Profit'].sum()
category_sales = df.groupby('Category')['Sales'].sum()

top_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(10)

# -----------------------------
# Dashboard
# -----------------------------
plt.figure(figsize=(24,14))

plt.subplot(3,4,1)
sns.boxplot(x=df['Sales'])
plt.title("Sales Distribution")

plt.subplot(3,4,2)
sns.boxplot(x=df['Profit'])
plt.title("Profit Distribution")

plt.subplot(3,4,3)
sns.boxplot(x=df['Discount'])
plt.title("Discount Distribution")

plt.subplot(3,4,4)
sns.scatterplot(x='Sales',y='Profit',data=df)
plt.title("Sales vs Profit")

plt.subplot(3,4,5)
monthly_sales.plot()
plt.title("Monthly Sales Trend")

plt.subplot(3,4,6)
monthly_profit.plot()
plt.title("Monthly Profit Trend")

plt.subplot(3,4,7)
region_sales.plot(kind='bar')
plt.title("Sales by Region")

plt.subplot(3,4,8)
category_profit.plot(kind='bar')
plt.title("Profit by Category")

plt.subplot(3,4,9)
category_sales.plot(kind='pie',autopct='%1.1f%%')
plt.title("Sales Share by Category")
plt.ylabel("")

plt.subplot(3,4,10)
sns.scatterplot(x='Discount',y='Profit',data=df)
plt.title("Discount Impact on Profit")

plt.subplot(3,4,11)
top_customers.plot(kind='bar')
plt.title("Top Customers by Sales")

plt.subplot(3,4,12)
plt.hist(df['Profit'],bins=50)
plt.title("Profit Distribution")

plt.suptitle("SUPERSTORE ANALYTICS DASHBOARD",fontsize=26)

plt.tight_layout(rect=[0,0,1,0.95])

plt.show()