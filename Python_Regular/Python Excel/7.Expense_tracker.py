from datetime import date
import csv

dt = date.today()
df = dt.strftime("%d/%m/%y")
samplecsv = "sample.csv"
expenses_data = []
stopped = False

with open(samplecsv, "w",newline="") as file:
    writer =csv.writer(file)
    while not stopped:
        enter_expenses = int(input("Enter a expenses(type 0 to stop): "))
        if enter_expenses==0:
            stopped = True
        else:
            writer.writerow([df, enter_expenses])
            expenses_data.append(enter_expenses)
print(f"expenses are:{expenses_data}")
print(f"total expenses is: {sum(expenses_data)}")

file.close()
