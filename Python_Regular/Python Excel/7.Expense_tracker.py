from datetime import date
import csv

dt = date.today()
df = dt.strftime("%d/%m/%y")
samplecsv = "sample.csv"
expenses_name = []
expenses_data = []

stopped = False

with open(samplecsv, "a",newline="") as file:
    writer =csv.writer(file)
    while not stopped:
        expenses_name= str(input("spended for(type 0 to stop): "))
        enter_expenses = int(input("Enter a expenses: "))
        if expenses_name==0:
            stopped = True
        else:
            writer.writerow([df,expenses_name, enter_expenses])
            expenses_data.append(enter_expenses)
print(f"expenses are:{expenses_data}")
print(f"total expenses is: {sum(expenses_data)}")

file.close()
