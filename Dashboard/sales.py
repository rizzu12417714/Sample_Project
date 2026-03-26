import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv(r"C:\C++ vs code\.vscode\Dashboard\Data.csv")



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
plt.show()
# 2️⃣ Profit by Product
plt.subplot(2,2,2)
df.groupby("product")["profit"].sum().plot(kind="bar")
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
# plt.show()
# 3️⃣ Units Sold Over Time
plt.subplot(2,2,3)
plt.plot(df["date"], df["units_sold"])
plt.title("Units Sold Over Time")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
# plt.show()
# 4️⃣ Revenue vs Profit
plt.subplot(2,2,4)
plt.scatter(df["revenue"], df["profit"])
plt.title("Revenue vs Profit")
plt.xlabel("Revenue")
plt.ylabel("Profit")

plt.tight_layout()
# plt.show()





