import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Banking_Data_100_Records.csv")
d=df.head(10)
print(d)
plt.bar(d['Loan Type'],d['Loan Amount'],color='g')
plt.title("Banking Data")
plt.xlabel("Loan Type")
plt.ylabel("Loan Amount")
plt.show()

plt.bar(d['Loan Type'],d['EMI'],color='y')
plt.title("Loan Amount EMI")
plt.xlabel("Loan Amount")
plt.ylabel("EMI")
plt.show()

x=["Loan Type"]
y=["Loan Amount"]
z=["Interest Rate"]
plt.plot(d['Loan Type'],d['Loan Amount'],marker='o',linestyle='--',label='Loan Amount')
plt.plot(d['Loan Type'],d['Interest Rate'],marker='s',linestyle='-',label='Interest Rate')
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.title("First Line Chart")
plt.legend()
plt.show()

plt.barh(d['Account Type'],d['Loan Amount'],color='r')
plt.title('Account Type Loan')
plt.xlabel("Account Type")
plt.ylabel("Loan Amount")
plt.show()

plt.pie(d['Loan Amount'],labels=d['Loan Type'],autopct='%1.1f%%')
plt.title("Loan Amount Type")
plt.show()



plt.plot(d['Loan Type'],d['Loan Amount'],marker='o',linestyle='--',label='Banking Data')
plt.xlabel=("Loan Type")
plt.ylabel=("Loan Amount")
plt.title("Banking Data")
plt.legend()
plt.show()
plt.figure()



