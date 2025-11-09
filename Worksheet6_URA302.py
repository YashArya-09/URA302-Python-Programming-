# Question 1.1

# import pandas as pd
# print("pandas version:", pd.__version__)
# print()

# Question 1.2

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# cities = ["New York", "Los Angeles", "Chicago"]
# df = pd.DataFrame({
#     "Name": names,
#     "Age": ages,
#     "City": cities
# })
# print(df)
# print()




# Question 2.1

# s1 = pd.Series([100, 200, 300, 400, 500])
# print(s1)
# print()

# Question 2.2

# print(s1.iloc[1])
# print(s1.iloc[3])
# print()

# Question 2.3

# s2 = pd.Series([10, 20, 30, 40, 50])
# print(s1 + s2)
# print()




# Question 3.1

# print(df[["Name", "City"]])
# print()

# Question 3.2

# salaries = [50000, 60000, 70000]
# df["Salary"] = salaries
# print(df)
# print()

# Question 3.3

# print(df["Age"].mean())
# print(df["Salary"].sum())
# print()




# Question 4.1

# data = {
#     "A": [10, 20, 30],
#     "B": [40, 50, 60],
#     "C": [70, 80, 90]
# }
# df2 = pd.DataFrame(data)
# print(df2)
# print()

# Question 4.2

# print(df2.describe())
# print()




# Question 5.1

# data = {
#     "Name": ["Ravi", "Neha", "Aman", "Simran"],
#     "Marks": [85, 90, 75, 95],
#     "Subject": ["Math", "Science", "English", "Math"]
# }
# df3 = pd.DataFrame(data)
# print(df3)
# print()

# Question 5.2

# print(df3[df3["Marks"] > 80])
# print()

# Question 5.3

# print(df3["Marks"].mean())
# print()




# Question 6.1

# df3.to_csv("student_data.csv", index=False)
# print("CSV file saved!")
# print()

# Question 6.2

# read_df = pd.read_csv("student_data.csv")
# print(read_df)
# print()




# Question 7.1

# print(read_df.sort_values("Marks"))
# print()

# Question 7.2 

# print(read_df.sort_values("Marks", ascending=False))
# print()



# Question 8.1

# print(read_df["Subject"].value_counts())
# print()

# Question 8.2

# print(read_df.groupby("Subject")["Marks"].mean())
# print()




# Question 9.1

# print(read_df.iloc[0])
# print()

# Question 9.2

# print(read_df.iloc[1:3])
# print()




# Question 10.1

# print(read_df.head(2))
# print()

# Question 10.2

# print(read_df.tail(2))
# print()