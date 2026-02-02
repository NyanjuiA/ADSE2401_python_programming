# Python script/file to demonstrate the various operations on Pandas Series.

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create and display a sample series
print("----1. Create and display a daily sales series ----")
sales = pd.Series([250,320,180,450,290,510,380],
                  index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
                  name='Daily Sales')
print(sales)
print("-" *50)

# 2. Basic mathematical operations on the 'Daily Sales' sample series
print("\n----2. Basic mathematical operations on the 'Daily Sales' daily sales series ----")
print(f"Original Sales:\n{sales}\n")
# Scalar operation to increase sales by 10%
print(f"Sales with a '10%' increase")
sales_increase = sales * 1.1
print(f"{sales_increase}\n")
# Element-wise operations
print(f"Sales minus 50")
sales_adjusted = sales - 50
print(f"{sales_adjusted}\n")
print("-" *50)

# 3. Series with series operations
print("----3. Series with series operations ----")
discounts = pd.Series([20,30,15,40,25,50,35],
                      index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
print(f"Discounts\n{discounts}")
print("-" *50)

# 4. Filtering and conditional operations
print("----4. Filtering and conditional operations ----")
print("Days with sales > 300")
high_sales = sales[sales > 300]
print(f"{high_sales}\n")
print(f"Weekend sales (i.e. Sat. & Sun.)")
weekend_sales = sales[['Sat','Sun']]
print(f"{weekend_sales}")
print("-" *50)

# 5. Statistcal operations
print("----5. Statistcal operations ----")
print(f"Total sales Kes. {sales.sum():.2f}")
print(f"Average sales Kes. {sales.mean():.2f}")
print(f"Highest sales Kes. {sales.max():.2f} on {sales.idxmax()}")
print(f"Lowest sales Kes. {sales.min():.2f} on {sales.idxmin()}")
print(f"Standard deviation: Kes. {sales.std():.2f}")
print("-" *50)

# 6. Applying Functions
print("----6. Applying Functions ----")
print(f"Applying square root to sales")
sqrt_sales = sales.apply(lambda x: round(np.sqrt(x),2))
print(f"{sqrt_sales}")
print("-" *50)

# 7. Missing Data Operations
print("----7. Missing Data Operations ----")
sales_with_na = pd.Series([250,None,180,450,None,510,380],
                          index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
print("Sales series with missing data")
print(sales_with_na)
print("Fill missing data/values with mean:")
filled_sales_series = sales_with_na.fillna(sales_with_na.mean())
print(f"{filled_sales_series}")
print("-" *50)



