import pandas as pd
df=pd.read_csv("Banking_Data_100_Records.csv",usecols=["Customer ID","Customer Name","Branch"])
print(df)

df1=pd.read_csv("Banking_Data_100_Records.csv",index_col="Customer Name")
print(df1)

df2=pd.read_csv("Banking_Data_100_Records.csv",na_values=["N/A","Unknown"])
print(df2)

df3=pd.read_csv("Banking_Data_100_Records.csv",sep='[:,:]',engine='python')
print(df3)

df4=pd.read_csv("Banking_Data_100_Records.csv",nrows=5)
print(df4)

df5=pd.read_csv("Banking_Data_100_Records.csv",skiprows=[4,5])
print(df5)
