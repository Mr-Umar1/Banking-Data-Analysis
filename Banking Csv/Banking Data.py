import csv
import random
from datetime import datetime,timedelta

# Output File Name

file_name="Banking_Data_100_Records.csv"

branches=["Bhusawal","Jalgaon","Nashik","Pune","Mumbai"]
account_types=["Savings","Current"]
genders=["Male","Female"]
loan_types=["Home","Car","Personal","Education"]
loan_statuses=["Approved","Rejected","Pending"]
transaction_types=["Deposit","Withdrawal","Transfer"]

first_names=["Amit","Rahul","Sneha","Pooja","Vikas","Neha","Rohit","Anjali","Sagar","Priya","Akash","Kiran","Meena","Rakesh","Komal","Nitin","Sachin","Swati","Deepak","Riya"]
last_names=["Sharma","Patil","Deshmukh","Joshi","Verma","Singh","Pawar","Gupta","Kulkarni","Yadav"]

relationship_managers=["Raj Patil","Sneha Joshi","Rohan Sharma","Priya Singh","Nitin Verma",]

header=["Customer ID","Customer Name","Branch","Account Type","Gender","Age","Loan Type","Loan Amount","Interest Rate","EMI","Salary","Credit Score","Loan Status","Transaction Type","Transaction Amount","Transaction Date","Balance","Relationship Manager"]

with open(file_name,"w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(header)
    start_date=datetime(2025,1,1)
    for i in range(1,101):
        customer_id=f"C{i:03}"
        customer_name=random.choice(first_names)+""+random.choice(last_names)
        branch=random.choice(branches)
        account_type=random.choice(account_types)
        gender=random.choice(account_types)
        gender=random.choice(genders)
        age=random.randint(21,60)
        loan_type=random.choice(loan_types)
        loan_amount=random.randrange(50000,2000001,5000)
        interest_rate=round(random.uniform(7.0,14.0),2)

        #Approximate EMI
        emi=round((loan_amount*interest_rate/100)/12+loan_amount/60,2)
        salary=random.randrange(20000,150001,1000)
        credit_score=random.randint(350,900)

        #Loan Status Logic
        if credit_score>=750:
            loan_status="Approved"
        elif credit_score>=650:
            loan_status=random.choice(["Approved","Pending"])
        else:
            loan_status=random.choice(["Rejected","Pending"])
        transaction_type=random.choice(transaction_types)
        transaction_amount=random.randrange(1000,200001,500)
        transaction_date=start_date+timedelta(days=random.randint(0,364))
        balance=random.randrange(5000,1000001,1000)
        relationship_manager=random.choice(relationship_managers)

        writer.writerow([customer_id,customer_name,branch,account_type,gender,age,loan_type,loan_amount,interest_rate,emi,salary,credit_score,loan_status,transaction_type,transaction_amount,transaction_date.strftime("%d-%m-%Y"),balance, relationship_manager])
print("================================")
print("Banking_Date_100_Records.csv Created Successfully!")
print("Total Records:100")
print("================================")




