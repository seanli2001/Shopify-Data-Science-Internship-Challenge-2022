import pandas as pd

df = pd.read_excel('questionOneData.xlsx')
total= df["total_items"].sum()
df= df["order_amount"]
print(df.sum()/total)




