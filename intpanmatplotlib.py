import pandas as pd
import numpy as np
# s=pd.Series([1,2,-3,4])
# print(s)
# print(np.square(s))
# a = s + [1000, 2000, 3000, 4000]
# print(a)
# print(s + 1000)
# print(s<0)



# s2 = pd.Series([68, 83, 112, 68])
# print(s2[[2]])



# s2 = pd.Series([68, 83, 112, 68] , index=["alice", "bob", "charles", "dwrwin"] )
# print(s2)

# weights = {"alice": 68, "bob": 83, "charles": 112, "dwrwin": 68}
# s3 = pd.Series(weights)
# print(s3)

# s4 = pd.Series(weights, index=["alice", "bob",])
# print(s4)


# print(s2+s3)
# s5 = pd.Series([1000,1000,1000,1000])
# print(s5)
# print(s2+s5)


# meaning = pd.Series(42,["life", "universe", "everything"])
# print(meaning)


# s6 = pd.Series([83, 68] , index=["bob", "alice"] , name="weights")
# print(s6)


#dff1=pd.DataFrame (ww,columns=["weight"])
#print(dff1)


# aa={ "a": [1,2,3], "b": [11,22,33]}
# dd=pd.DataFrame(aa)
# print(dd)



#ploting a series
# import matplotlib.pyplot as plt
# temperatures = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.8, 3.4]
# s7 = pd.Series(temperatures, name="temperature")
# s7.plot()
# plt.show()

# h=[3,6,2,5,7,8,9,1,4]
# hh=pd.Series(h, name="hh" , index=["a","b","c","d","e","f","g","h","i"])
# hh.plot()
# plt.show()



# #Creating a DataFrame - pass a dictionary of series objects
# people_dict = {
# "weights" : pd.Series([68, 83, 112, 68], index=["alice", "bob", "charles", "dwrwin"]) ,
# "birthyear": pd.Series([1986, 1990, 1982, 1990], index=["alice", "bob", "charles", "dwrwin"]) ,
# "childern": pd.Series([0, 2, 3, 1], index=["alice", "bob", "charles", "dwrwin"]) ,
# "hobby": pd.Series(["tennis", "golf", "chess", "tennis"], index=["alice", "bob", "charles", "dwrwin"]) ,
# }

# #print(people_dict)
# df=pd.DataFrame(people_dict)
# print(df)

# #dataFrame - access a column
# print(df["birthyear"])
# #DataFrame - Access the multiple columns
# print(df[["birthyear", "hobby"]])






# # date 12-02-2026







# d2 = pd.DataFrame(people_dict, columns=["birthyear", "weight" ] , index = ["bob", "alice", "eugene"])
# print(d2)


# #accessing the row

# print (df.loc["charles"])
# print(df.iloc[2])


# #DataFrame - Get a slice of rows

# print("get a slice of row")
# print(df.iloc[1:3])

# #DataFrame - Pass a boolean array

# print("passing a boolean array TFT")

# #print(df[np.array([True, False, True])])
# print(df[[True, False, True, False]])


# print ("...........")

# print(df[df["birthyear"]  <  1990])
# #Adding and removing columns
# #Adds a new column "age"

# print("............")
# df["age"] = 2016 - df["birthyear"]
# print(df)

# #Adds another column "over 30"

# print(".............")
# df["over 30"] = df["age"] > 30
# print(df)
 

# print("........")


# df["pets"] = pd.Series(["cat", "dog", "dog", "cat"], index=["alice", "bob", "charles", "dwrwin"])
# print(df)



# #DataFrame - Add new column using insert method after an existing column
# print(".............")
# df.insert(2, "height",[123,176, 165, 180])
# print(df)

# print(".............")
# #DataFrame - Sort the DataFrame by a column
# s=df.sort_index(ascending=False)
# print(s)
# print(df)


# print(".............")

# #print(df.sort_index(inplace=True))
# #print(df.sort_index(inplace=True))  its output will be None as func didnot return anything but it will sort the df in place
# print(".............")
# df.sort_index(inplace=True, ascending=False)
# print(df)

# #DataFrame - Sort the DataFrame by a column sort by value of age
# print(".............")
# df.sort_values(by="age", inplace=True)
# print(df)

# print(".............")


# #Ploting DataFrame
# df.plot( kind = "line", x="age", y=["weights", "height"])
# plt.show()




# #DataFrame - Saving
# #Lets Create a new DataFrame my_df and save it

# my_df = pd.DataFrame( [
#     ["biking", 68.5,1985,np.nan],
#     ["Dancing", 83.2,1990,3]

# ],
# columns=["hobby", "weight", "birthyear", "childern"] , index=["alice", "bob"])
# print(my_df)

# #Saving the DataFrame to a csv file
# my_df.to_csv("my_df.csv")




# print(" .............................................")



# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = "o")
# plt.show()
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = '*')
# plt.show()


# print("........................")


import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()


# x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40 ]
# num_bins = 5

# plt.hist (x, num_bins, facecolor='blue')
# plt.show()

# x = np.array([5, 7, 8, 7, 2, 4, 17, 2, 9, 4, 11, 12, 9, 6])
# y = np.array([99, 86, 78, 88, 101, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# plt.scatter(x, y, color = 'hotpink')
# plt.show()



# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "hotpink", width=0.7)
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y, color = "hotpink", height=0.7)
# plt.show()



# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels, startangle=90)
# plt.show()



# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]   
# myexplode = [0.4, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show()


import seaborn as sns


# data = [1,2,2,2,3,3,4,5,5,5,5,6,7,8,9,10]
# sns.kdeplot(data, fill=True, color="blue")
# plt.title("Kernel Density Estimation (KDE) Plot")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.show()
# data = pd.read_csv(".vscode/tips_unclean.csv")

# print(data.head())
# sns.boxplot(y=data['total_bill'])

# plt.show(block=False)
# plt.figure()
# sns.lineplot(x="sex", y="total_bill", data=data)
# plt.title('Title using Matplotlib Function')
# plt.show(block=False)
# plt.figure()
# sns.lineplot(x="day", y="tip", data=data)
# plt.show(block=False)
# sns.barplot(x="day", y="total_bill", data=data)
# plt.show()
# sns.histplot(x="total_bill", data=data)
# plt.show()
# sns.countplot(data["day"])
# plt.show()
# sns.kdeplot(x=data["total_bill"], fill=True, color="blue")
# plt.show()
# sns.pairplot(data, hue="sex", diag_kind="kde")
# plt.show()
# sns.pairplot(data, hue="day")
# plt.show()


# data1 = [10, 20, 30, 40, 50]
# data2 = [5, 25, 35, 45, 55]  
# df = pd.DataFrame({"Data1": data1, "Data2": data2})
# print("\n Covariance:")  
# print(df.cov())  
# print("\n Correlation:")
# print(df.corr())


# df = pd.read_csv(r"C:\C++ vs code\.vscode\StudentsPerformance.csv")
# print(df)
# correlation_matrix = df.corr(numeric_only=True)
# print("Correlation Matrix:\n", correlation_matrix)

# covariance_matrix = df.cov(numeric_only=True)
# print("Covariance Matrix:\n", covariance_matrix)
# # plt.figure(figsize=(10, 6))
# plt.figure()
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
# plt.title("Correlation Matrix Heatmap")
# plt.show()

#Generating some data with an outlier
# data = [10, 12, 14, 15, 18, 20, 22, 25, 100]

# df = pd.DataFrame(data, columns=["Values"])
# print(df)
# # Calculate the first quartile (Q1), third quartile (Q3), and interquartile range (IQR)
# Q1 = df["Values"].quantile(0.25)
# Q3 = df["Values"].quantile(0.75)
# IQR = Q3 - Q1
# # Define the lower and upper bounds for outliers
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# print("Lower Bound:", lower_bound)
# print("Upper Bound:", upper_bound)
# #Detect outliers
# outliers = df[(df["Values"] < lower_bound) | (df["Values"] > upper_bound)]
# print("Outliers:\n", outliers)



# data = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2, 2, 3, 1, 1, 2 ]
# mean = np.mean(data)
# std = np.std(data)
# print("mean of the dataset is", mean)
# print("standard deviation of the dataset is", std)

# threshold = 3
# outliers = []   
# for i in data:
#     z_score = (i - mean) / std
#     if abs(z_score) > threshold:
#         outliers.append(i)
# print("Outlier in dataset is ", outliers)


# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x, y)
# plt.title("abc")

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x, y)
# plt.title("def")
# plt.tight_layout()

# plt.suptitle("overall data")
# plt.show()




# df.to_excel("output.xlsx", index=False)



#DATE 25-03-2026


#Load a dataset from seaborn library

# df = sns.load_dataset("iris")
# #first 5 rows of the dataset
# print("First 5 rows:")

# print(df.head())
# #Dataset shape  
# print("\nShape:", df.shape )
# #Dataset info
# print("\nInfo:")
# print(df.info())
# #Summary statistics
# print("\nSummary Statistics:")
# print(df.describe())

# #Check for missing values
# print("\nMissing Values:")
# print(df.isnull().sum())

# #Unique values in a column
# print("\nUnique Species:")
# print(df['species'].unique())


# print("\nCorrelation Matrix:")
# print(df.corr(numeric_only=True ))



# histogram of sepal_length
# sns.histplot(df["sepal_length"])
# plt.show()

# Scatter plot of sepal_length vs sepal_width colored by species
# plt.figure()
# sns.scatterplot(x="sepal_length", y="sepal_width", hue = "species", data=df)
# plt.show()

# Boxplot of petal_length by species
# plt.figure()
# sns.boxplot(x="species", y="petal_length", data=df)
# plt.show()

# Pairplot

# sns.pairplot(df, hue="species")
# plt.show()

# Correlation matrix heatmap


# sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
# plt.show()




#Outlier Detection and Removal
# df = pd.read_csv(r"C:\C++ vs code\.vscode\StudentsPerformance.csv") 
# print(df)

# columns = "math score"

# plt.figure(figsize=(8, 5))
# sns.boxplot(x=df[columns])
# plt.title("boxplot for Outlier Detection")

# # Calculate the first quartile (Q1), third quartile (Q3), and interquartile range (IQR)          
# Q1 = df[columns].quantile(0.25)
# print("Q1:", Q1)
# Q3 = df[columns].quantile(0.75)
# print("Q3:", Q3)
# IQR = Q3 - Q1
# print("IQR:", IQR)
# # Define the lower and upper bounds for outliers
# lower_bound = Q1 - 1.5 * IQR
# print("Lower Bound:", lower_bound)
# upper_bound = Q3 + 1.5 * IQR
# print("Upper Bound:", upper_bound)
# #identify outliers
# outliers = df[(df[columns] < lower_bound) | (df[columns] > upper_bound)]
# print("Outliers:\n", outliers)
# # Removeing outliers
# df_clean = df[(df[columns] >= lower_bound) & (df[columns] <= upper_bound)]


#DATE 26-03-2026





from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


tips = sns.load_dataset("tips")

X = tips[["total_bill"]]
y = tips["tip"] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
