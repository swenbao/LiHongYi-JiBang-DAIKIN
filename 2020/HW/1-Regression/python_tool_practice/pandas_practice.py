# 載入 pandas 套件
import pandas as pd

# # 建立 series
# data = pd.Series([20, 10, 15, 40])
# print(data)
# # 基本 series 操作
# print("Sum :", data.sum())
# print("Mean :",data.mean())
# print("Median :",data.median())
# print("Describe :",data.describe())

# data*=2
# print(data)

# compare = data == 20
# print(compare)

# 建立 data frame
data = pd.DataFrame({
    "name":["Amy", "John", "Bob"],
    "salary":[30000, 50000, 40000],
    "age":[25, 30, 35]
})

# 基本 data frame 操作
print(data)
print("=========")

# 取得特定的欄位
# print(data["name"])
print(data["salary"])

# 取得特定的列
print(data.iloc[0])
# print(data.iloc[1])
# print(data.iloc[2])

# 取得特定的列
print(data.iloc[0:2])
print(data.iloc[1:3])
print("==========")
print(data.iloc[:, 0:3])
print(data.iloc[:, 1:3])
