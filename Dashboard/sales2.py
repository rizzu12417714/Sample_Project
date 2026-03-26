import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("fitness.csv")

# Check missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Create Dashboard
plt.figure(figsize=(14,10))

# 1️⃣ Duration vs Calories
plt.subplot(2,2,1)
plt.scatter(df["Duration"], df["Calories"])
plt.title("Duration vs Calories")
plt.xlabel("Duration")
plt.ylabel("Calories")

# 2️⃣ Pulse vs Calories
plt.subplot(2,2,2)
plt.scatter(df["Pulse"], df["Calories"])
plt.title("Pulse vs Calories")
plt.xlabel("Pulse")
plt.ylabel("Calories")

# 3️⃣ Average Calories by Duration
plt.subplot(2,2,3)
df.groupby("Duration")["Calories"].mean().plot(kind="bar")
plt.title("Average Calories by Duration")
plt.xlabel("Duration")
plt.ylabel("Average Calories")

# 4️⃣ Duration Distribution
plt.subplot(2,2,4)
plt.hist(df["Duration"])
plt.title("Duration Distribution")
plt.xlabel("Duration")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
