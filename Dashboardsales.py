import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data2.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Create Figure
plt.figure(figsize=(14,10))

# 1️⃣ Revenue by Region
plt.subplot(2,2,1)
df.groupby("region")["revenue"].sum().plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

# 2️⃣ Profit by Product
plt.subplot(2,2,2)
df.groupby("product")["profit"].sum().plot(kind="bar")
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")

# 3️⃣ Units Sold Over Time
plt.subplot(2,2,3)
plt.plot(df["date"], df["units_sold"])
plt.title("Units Sold Over Time")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)

# 4️⃣ Revenue vs Profit
plt.subplot(2,2,4)
plt.scatter(df["revenue"], df["profit"])
plt.title("Revenue vs Profit")
plt.xlabel("Revenue")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()
