num = int(input("Enter a table u want:"))
table1 = [(x+1) * num for x in range(20) ]
#table2 = [str(x) '*' str(num) '=' str(x*num) for  x in range(20)]
table3 = [f"{(num)}*{(x+1)}={(x+1)*num}" for x in range(20)]

print(table3)